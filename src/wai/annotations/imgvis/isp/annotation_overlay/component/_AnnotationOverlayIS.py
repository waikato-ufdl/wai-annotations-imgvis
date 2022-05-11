import io
import numpy as np
import PIL

from PIL import ImageDraw

from wai.common.cli.options import TypedOption
from wai.annotations.core.component import ProcessorComponent
from wai.annotations.core.stream import ThenFunction, DoneFunction
from wai.annotations.core.stream.util import RequiresNoFinalisation
from wai.annotations.domain.image import Image
from wai.annotations.domain.image.segmentation import ImageSegmentationInstance
from wai.annotations.imgvis.isp.annotation_overlay.component._colors import default_colors


class AnnotationOverlayIS(
    RequiresNoFinalisation,
    ProcessorComponent[ImageSegmentationInstance, ImageSegmentationInstance]
):
    """
    Stream processor which adds image classification labels on top of images.
    """

    BYTE_PLACE_MULTIPLIER = np.array([list(1 << i for i in reversed(range(8)))], np.uint8)

    labels: str = TypedOption(
        "--labels",
        type=str,
        default="",
        help="the comma-separated list of labels of annotations to overlay, leave empty to overlay all"
    )

    alpha: int = TypedOption(
        "--alpha",
        type=int,
        default=64,
        help="the alpha value to use for overlaying the annotations (0: transparent, 255: opaque)."
    )

    colors: str = TypedOption(
        "--colors",
        type=str,
        default="",
        help="the blank-separated list of RGB triplets (R,G,B) of custom colors to use, leave empty for default colors"
    )

    def _initialize(self):
        """
        Initializes colors etc.
        """
        self._colors = dict()
        self._default_colors = default_colors()
        self._default_colors_index = 0
        self._custom_colors = []
        if len(self.colors) > 0:
            for color in self.colors.split(" "):
                self._custom_colors.append([int(x) for x in color.split(",")])
        self._accepted_labels = None
        if len(self.labels) > 0:
            self._accepted_labels = set(self.labels.split(","))

    def _next_default_color(self):
        """
        Returns the next default color.

        :return: the color tuple
        :rtype: tuple
        """
        if self._default_colors_index >= len(self._default_colors):
            self._default_colors_index = 0
        result = self._default_colors[self._default_colors_index]
        self._default_colors_index += 1
        return result

    def _get_color(self, label):
        """
        Returns the color for the label.

        :param label: the label to get the color for
        :type label: str
        :return: the RGBA color tuple
        :rtype: tuple
        """
        if label not in self._colors:
            has_custom = False
            if label in self._label_mapping:
                index = self._label_mapping[label]
                if index < len(self._custom_colors):
                    has_custom = True
                    self._colors[label] = self._custom_colors[index]
            if not has_custom:
                self._colors[label] = self._next_default_color()
        r, g, b = self._colors[label]
        return r, g, b, self.alpha

    def process_element(
            self,
            element: ImageSegmentationInstance,
            then: ThenFunction[ImageSegmentationInstance],
            done: DoneFunction
    ):
        if not hasattr(self, "_colors"):
            self._initialize()

        img_in = element.data
        img_pil = element.data.pil_image

        # create label/index mapping for custom colors
        self._label_mapping = dict()
        for index, label in enumerate(element.annotations.labels):
            self._label_mapping[label] = index

        # create overlay for annotations
        overlay = PIL.Image.new('RGBA', img_pil.size, (0, 0, 0, 0))
        draw = ImageDraw.Draw(overlay)

        label_images = element.annotations.label_images
        updated = False
        for label in label_images:
            # skip label?
            if (self._accepted_labels is not None) and (label not in self._accepted_labels):
                continue
            # draw overlay
            updated = True
            mask = label_images[label]
            draw.bitmap((0, 0), mask, fill=self._get_color(label))

        if updated:
            # add overlay
            img_pil.paste(overlay, (0, 0), mask=overlay)
            # convert back to PIL bytes
            pil_img_bytes = io.BytesIO()
            img_pil.save(pil_img_bytes, format=img_in.format.pil_format_string)
            img_out = Image(img_in.filename, pil_img_bytes.getvalue(), img_in.format, img_in.size)

            # new element
            then(element.__class__(img_out, element.annotations))
        else:
            then(element)
