from document_recognition.template import Template
from tests.conftest import TEMPLATE_XML


def test_read_xml(template: Template) -> None:
    template_ = Template.from_xml(TEMPLATE_XML)

    assert template_ == template
