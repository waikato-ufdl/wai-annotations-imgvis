from typing import Type, Tuple

from wai.annotations.core.component import ProcessorComponent
from wai.annotations.core.domain import DomainSpecifier
from wai.annotations.core.specifier import ProcessorStageSpecifier


class AnnotationOverlayODISPSpecifier(ProcessorStageSpecifier):
    """
    Specifies the annotation_overlay image ISP.
    """
    @classmethod
    def description(cls) -> str:
        return "Adds object detection overlays to images passing through."

    @classmethod
    def domain_transfer_function(
            cls,
            input_domain: Type[DomainSpecifier]
    ) -> Type[DomainSpecifier]:
        from wai.annotations.domain.image.object_detection import ImageObjectDetectionDomainSpecifier
        if input_domain is ImageObjectDetectionDomainSpecifier:
            return input_domain
        else:
            raise Exception(
                f"AnnotationOverlayOD only handles the following domains: "
                f"{ImageObjectDetectionDomainSpecifier.name()}"
            )

    @classmethod
    def components(cls) -> Tuple[Type[ProcessorComponent]]:
        from wai.annotations.imgvis.isp.annotation_overlay.component import AnnotationOverlayOD
        return AnnotationOverlayOD,
