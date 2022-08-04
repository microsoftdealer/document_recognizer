import datetime
from typing import Any, Dict

import pytest

from document_recognition.backends import ApiResponse
from document_recognition.backends.base import TextAnnotations, Vertices
from document_recognition.entities.drive_license import DriverLicense
from document_recognition.entities.passport import Passport
from document_recognition.recognizers.synchronous.driver_license_recognizer import (
    DriverLicenseRecognizerByTemplate,
)
from document_recognition.recognizers.synchronous.passport_recognizer import (
    PassportRecognizerByRegularExpression,
)
from tests.mocked_sync_client import MockedSyncDocumentRecognition


def dict_to_driver_license_with_sep(document: Dict[str, Any], sep: str):
    document_entity_with_sep = {}
    for key, value in document.items():
        if isinstance(value, list):
            document_entity_with_sep[key] = sep.join(value)
        else:
            document_entity_with_sep[key] = value
    return DriverLicense(**document_entity_with_sep)


# TODO move parametrize to files
@pytest.mark.parametrize(
    "response,document_entity",
    [
        (
            ApiResponse(
                text_annotations=[
                    TextAnnotations(
                        text="RUS\nР\nводитЕЛЬСКОЕ УДОСТОВЕРЕНИ\n1. БАБАЯН\nBABAYAN\n2. САМВЕЛ ЮРЬЕВИЧ\nSAMVEL YUR'YEVICH\n3. 01.07.1980\nКРАСНОДАРСКИЙ КРАЙ\nKRASNODARSKIY KRAY\n4a) 23.09.2015\n4c) ГИБДД 2327\nGIBDD 2327\n9.\n23.09.2025\n5. 2322803756\n8. ХАНТЫ-МАНСИЙСКИЙ АО - ЮГРА\nKHANTY-MANSIYSKIY AO-YUGRA\n881 CC1M",
                        vertices=[
                            Vertices(x=67, y=29),
                            Vertices(x=579, y=29),
                            Vertices(x=579, y=331),
                            Vertices(x=67, y=331),
                        ],
                        locale=None,
                        mid=None,
                        score=None,
                        confidence=None,
                        topicality=None,
                    ),
                    TextAnnotations(
                        text="RUS",
                        vertices=[
                            Vertices(x=81, y=40),
                            Vertices(x=128, y=40),
                            Vertices(x=128, y=54),
                            Vertices(x=81, y=54),
                        ],
                        locale=None,
                        mid=None,
                        score=None,
                        confidence=None,
                        topicality=None,
                    ),
                    TextAnnotations(
                        text="Р",
                        vertices=[
                            Vertices(x=159, y=110),
                            Vertices(x=157, y=212),
                            Vertices(x=68, y=210),
                            Vertices(x=70, y=108),
                        ],
                        locale=None,
                        mid=None,
                        score=None,
                        confidence=None,
                        topicality=None,
                    ),
                    TextAnnotations(
                        text="водитЕЛЬСКОЕ",
                        vertices=[
                            Vertices(x=211, y=29),
                            Vertices(x=384, y=30),
                            Vertices(x=384, y=63),
                            Vertices(x=211, y=62),
                        ],
                        locale=None,
                        mid=None,
                        score=None,
                        confidence=None,
                        topicality=None,
                    ),
                    TextAnnotations(
                        text="УДОСТОВЕРЕНИ",
                        vertices=[
                            Vertices(x=395, y=30),
                            Vertices(x=579, y=31),
                            Vertices(x=579, y=64),
                            Vertices(x=395, y=63),
                        ],
                        locale=None,
                        mid=None,
                        score=None,
                        confidence=None,
                        topicality=None,
                    ),
                    TextAnnotations(
                        text="1.",
                        vertices=[
                            Vertices(x=222, y=79),
                            Vertices(x=232, y=79),
                            Vertices(x=232, y=93),
                            Vertices(x=222, y=93),
                        ],
                        locale=None,
                        mid=None,
                        score=None,
                        confidence=None,
                        topicality=None,
                    ),
                    TextAnnotations(
                        text="БАБАЯН",
                        vertices=[
                            Vertices(x=249, y=79),
                            Vertices(x=315, y=79),
                            Vertices(x=315, y=93),
                            Vertices(x=249, y=93),
                        ],
                        locale=None,
                        mid=None,
                        score=None,
                        confidence=None,
                        topicality=None,
                    ),
                    TextAnnotations(
                        text="BABAYAN",
                        vertices=[
                            Vertices(x=247, y=99),
                            Vertices(x=318, y=99),
                            Vertices(x=318, y=109),
                            Vertices(x=247, y=109),
                        ],
                        locale=None,
                        mid=None,
                        score=None,
                        confidence=None,
                        topicality=None,
                    ),
                    TextAnnotations(
                        text="2.",
                        vertices=[
                            Vertices(x=221, y=117),
                            Vertices(x=230, y=117),
                            Vertices(x=230, y=127),
                            Vertices(x=221, y=127),
                        ],
                        locale=None,
                        mid=None,
                        score=None,
                        confidence=None,
                        topicality=None,
                    ),
                    TextAnnotations(
                        text="САМВЕЛ",
                        vertices=[
                            Vertices(x=247, y=117),
                            Vertices(x=315, y=117),
                            Vertices(x=315, y=127),
                            Vertices(x=247, y=127),
                        ],
                        locale=None,
                        mid=None,
                        score=None,
                        confidence=None,
                        topicality=None,
                    ),
                    TextAnnotations(
                        text="ЮРЬЕВИЧ",
                        vertices=[
                            Vertices(x=323, y=117),
                            Vertices(x=406, y=117),
                            Vertices(x=406, y=127),
                            Vertices(x=323, y=127),
                        ],
                        locale=None,
                        mid=None,
                        score=None,
                        confidence=None,
                        topicality=None,
                    ),
                    TextAnnotations(
                        text="SAMVEL",
                        vertices=[
                            Vertices(x=247, y=134),
                            Vertices(x=309, y=134),
                            Vertices(x=309, y=145),
                            Vertices(x=247, y=145),
                        ],
                        locale=None,
                        mid=None,
                        score=None,
                        confidence=None,
                        topicality=None,
                    ),
                    TextAnnotations(
                        text="YUR'YEVICH",
                        vertices=[
                            Vertices(x=314, y=134),
                            Vertices(x=409, y=134),
                            Vertices(x=409, y=145),
                            Vertices(x=314, y=145),
                        ],
                        locale=None,
                        mid=None,
                        score=None,
                        confidence=None,
                        topicality=None,
                    ),
                    TextAnnotations(
                        text="3.",
                        vertices=[
                            Vertices(x=219, y=153),
                            Vertices(x=232, y=153),
                            Vertices(x=232, y=163),
                            Vertices(x=219, y=163),
                        ],
                        locale=None,
                        mid=None,
                        score=None,
                        confidence=None,
                        topicality=None,
                    ),
                    TextAnnotations(
                        text="01.07.1980",
                        vertices=[
                            Vertices(x=245, y=152),
                            Vertices(x=318, y=153),
                            Vertices(x=318, y=164),
                            Vertices(x=245, y=163),
                        ],
                        locale=None,
                        mid=None,
                        score=None,
                        confidence=None,
                        topicality=None,
                    ),
                    TextAnnotations(
                        text="КРАСНОДАРСКИЙ",
                        vertices=[
                            Vertices(x=245, y=169),
                            Vertices(x=390, y=169),
                            Vertices(x=390, y=182),
                            Vertices(x=245, y=182),
                        ],
                        locale=None,
                        mid=None,
                        score=None,
                        confidence=None,
                        topicality=None,
                    ),
                    TextAnnotations(
                        text="КРАЙ",
                        vertices=[
                            Vertices(x=397, y=169),
                            Vertices(x=437, y=169),
                            Vertices(x=437, y=182),
                            Vertices(x=397, y=182),
                        ],
                        locale=None,
                        mid=None,
                        score=None,
                        confidence=None,
                        topicality=None,
                    ),
                    TextAnnotations(
                        text="KRASNODARSKIY",
                        vertices=[
                            Vertices(x=245, y=189),
                            Vertices(x=380, y=189),
                            Vertices(x=380, y=199),
                            Vertices(x=245, y=199),
                        ],
                        locale=None,
                        mid=None,
                        score=None,
                        confidence=None,
                        topicality=None,
                    ),
                    TextAnnotations(
                        text="KRAY",
                        vertices=[
                            Vertices(x=386, y=189),
                            Vertices(x=429, y=189),
                            Vertices(x=429, y=199),
                            Vertices(x=386, y=199),
                        ],
                        locale=None,
                        mid=None,
                        score=None,
                        confidence=None,
                        topicality=None,
                    ),
                    TextAnnotations(
                        text="4a",
                        vertices=[
                            Vertices(x=217, y=206),
                            Vertices(x=234, y=206),
                            Vertices(x=234, y=216),
                            Vertices(x=217, y=216),
                        ],
                        locale=None,
                        mid=None,
                        score=None,
                        confidence=None,
                        topicality=None,
                    ),
                    TextAnnotations(
                        text=")",
                        vertices=[
                            Vertices(x=233, y=206),
                            Vertices(x=238, y=206),
                            Vertices(x=238, y=216),
                            Vertices(x=233, y=216),
                        ],
                        locale=None,
                        mid=None,
                        score=None,
                        confidence=None,
                        topicality=None,
                    ),
                    TextAnnotations(
                        text="23.09.2015",
                        vertices=[
                            Vertices(x=244, y=206),
                            Vertices(x=317, y=206),
                            Vertices(x=317, y=216),
                            Vertices(x=244, y=216),
                        ],
                        locale=None,
                        mid=None,
                        score=None,
                        confidence=None,
                        topicality=None,
                    ),
                    TextAnnotations(
                        text="4c",
                        vertices=[
                            Vertices(x=217, y=223),
                            Vertices(x=229, y=223),
                            Vertices(x=229, y=237),
                            Vertices(x=217, y=237),
                        ],
                        locale=None,
                        mid=None,
                        score=None,
                        confidence=None,
                        topicality=None,
                    ),
                    TextAnnotations(
                        text=")",
                        vertices=[
                            Vertices(x=233, y=223),
                            Vertices(x=237, y=223),
                            Vertices(x=237, y=237),
                            Vertices(x=233, y=237),
                        ],
                        locale=None,
                        mid=None,
                        score=None,
                        confidence=None,
                        topicality=None,
                    ),
                    TextAnnotations(
                        text="ГИБДД",
                        vertices=[
                            Vertices(x=244, y=223),
                            Vertices(x=301, y=223),
                            Vertices(x=301, y=237),
                            Vertices(x=244, y=237),
                        ],
                        locale=None,
                        mid=None,
                        score=None,
                        confidence=None,
                        topicality=None,
                    ),
                    TextAnnotations(
                        text="2327",
                        vertices=[
                            Vertices(x=306, y=223),
                            Vertices(x=339, y=223),
                            Vertices(x=339, y=237),
                            Vertices(x=306, y=237),
                        ],
                        locale=None,
                        mid=None,
                        score=None,
                        confidence=None,
                        topicality=None,
                    ),
                    TextAnnotations(
                        text="GIBDD",
                        vertices=[
                            Vertices(x=243, y=241),
                            Vertices(x=292, y=241),
                            Vertices(x=292, y=253),
                            Vertices(x=243, y=253),
                        ],
                        locale=None,
                        mid=None,
                        score=None,
                        confidence=None,
                        topicality=None,
                    ),
                    TextAnnotations(
                        text="2327",
                        vertices=[
                            Vertices(x=298, y=241),
                            Vertices(x=330, y=241),
                            Vertices(x=330, y=253),
                            Vertices(x=298, y=253),
                        ],
                        locale=None,
                        mid=None,
                        score=None,
                        confidence=None,
                        topicality=None,
                    ),
                    TextAnnotations(
                        text="9",
                        vertices=[
                            Vertices(x=215, y=314),
                            Vertices(x=218, y=314),
                            Vertices(x=218, y=324),
                            Vertices(x=215, y=324),
                        ],
                        locale=None,
                        mid=None,
                        score=None,
                        confidence=None,
                        topicality=None,
                    ),
                    TextAnnotations(
                        text=".",
                        vertices=[
                            Vertices(x=220, y=314),
                            Vertices(x=223, y=314),
                            Vertices(x=223, y=324),
                            Vertices(x=220, y=324),
                        ],
                        locale=None,
                        mid=None,
                        score=None,
                        confidence=None,
                        topicality=None,
                    ),
                    TextAnnotations(
                        text="23.09.2025",
                        vertices=[
                            Vertices(x=444, y=207),
                            Vertices(x=517, y=207),
                            Vertices(x=517, y=217),
                            Vertices(x=444, y=217),
                        ],
                        locale=None,
                        mid=None,
                        score=None,
                        confidence=None,
                        topicality=None,
                    ),
                    TextAnnotations(
                        text="5.",
                        vertices=[
                            Vertices(x=215, y=261),
                            Vertices(x=227, y=261),
                            Vertices(x=227, y=271),
                            Vertices(x=215, y=271),
                        ],
                        locale=None,
                        mid=None,
                        score=None,
                        confidence=None,
                        topicality=None,
                    ),
                    TextAnnotations(
                        text="2322803756",
                        vertices=[
                            Vertices(x=241, y=261),
                            Vertices(x=322, y=261),
                            Vertices(x=322, y=271),
                            Vertices(x=241, y=271),
                        ],
                        locale=None,
                        mid=None,
                        score=None,
                        confidence=None,
                        topicality=None,
                    ),
                    TextAnnotations(
                        text="8.",
                        vertices=[
                            Vertices(x=215, y=276),
                            Vertices(x=226, y=276),
                            Vertices(x=226, y=290),
                            Vertices(x=215, y=290),
                        ],
                        locale=None,
                        mid=None,
                        score=None,
                        confidence=None,
                        topicality=None,
                    ),
                    TextAnnotations(
                        text="ХАНТЫ",
                        vertices=[
                            Vertices(x=241, y=276),
                            Vertices(x=290, y=276),
                            Vertices(x=290, y=290),
                            Vertices(x=241, y=290),
                        ],
                        locale=None,
                        mid=None,
                        score=None,
                        confidence=None,
                        topicality=None,
                    ),
                    TextAnnotations(
                        text="-",
                        vertices=[
                            Vertices(x=300, y=276),
                            Vertices(x=310, y=276),
                            Vertices(x=310, y=290),
                            Vertices(x=300, y=290),
                        ],
                        locale=None,
                        mid=None,
                        score=None,
                        confidence=None,
                        topicality=None,
                    ),
                    TextAnnotations(
                        text="МАНСИЙСКИЙ",
                        vertices=[
                            Vertices(x=311, y=276),
                            Vertices(x=433, y=276),
                            Vertices(x=433, y=290),
                            Vertices(x=311, y=290),
                        ],
                        locale=None,
                        mid=None,
                        score=None,
                        confidence=None,
                        topicality=None,
                    ),
                    TextAnnotations(
                        text="АО",
                        vertices=[
                            Vertices(x=439, y=276),
                            Vertices(x=461, y=276),
                            Vertices(x=461, y=290),
                            Vertices(x=439, y=290),
                        ],
                        locale=None,
                        mid=None,
                        score=None,
                        confidence=None,
                        topicality=None,
                    ),
                    TextAnnotations(
                        text="-",
                        vertices=[
                            Vertices(x=467, y=276),
                            Vertices(x=470, y=276),
                            Vertices(x=470, y=290),
                            Vertices(x=467, y=290),
                        ],
                        locale=None,
                        mid=None,
                        score=None,
                        confidence=None,
                        topicality=None,
                    ),
                    TextAnnotations(
                        text="ЮГРА",
                        vertices=[
                            Vertices(x=477, y=277),
                            Vertices(x=523, y=277),
                            Vertices(x=523, y=291),
                            Vertices(x=477, y=291),
                        ],
                        locale=None,
                        mid=None,
                        score=None,
                        confidence=None,
                        topicality=None,
                    ),
                    TextAnnotations(
                        text="KHANTY",
                        vertices=[
                            Vertices(x=242, y=296),
                            Vertices(x=304, y=296),
                            Vertices(x=304, y=306),
                            Vertices(x=242, y=306),
                        ],
                        locale=None,
                        mid=None,
                        score=None,
                        confidence=None,
                        topicality=None,
                    ),
                    TextAnnotations(
                        text="-",
                        vertices=[
                            Vertices(x=310, y=296),
                            Vertices(x=316, y=296),
                            Vertices(x=316, y=306),
                            Vertices(x=310, y=306),
                        ],
                        locale=None,
                        mid=None,
                        score=None,
                        confidence=None,
                        topicality=None,
                    ),
                    TextAnnotations(
                        text="MANSIYSKIY",
                        vertices=[
                            Vertices(x=320, y=296),
                            Vertices(x=415, y=296),
                            Vertices(x=415, y=306),
                            Vertices(x=320, y=306),
                        ],
                        locale=None,
                        mid=None,
                        score=None,
                        confidence=None,
                        topicality=None,
                    ),
                    TextAnnotations(
                        text="AO",
                        vertices=[
                            Vertices(x=420, y=296),
                            Vertices(x=442, y=296),
                            Vertices(x=442, y=306),
                            Vertices(x=420, y=306),
                        ],
                        locale=None,
                        mid=None,
                        score=None,
                        confidence=None,
                        topicality=None,
                    ),
                    TextAnnotations(
                        text="-",
                        vertices=[
                            Vertices(x=446, y=296),
                            Vertices(x=453, y=296),
                            Vertices(x=453, y=306),
                            Vertices(x=446, y=306),
                        ],
                        locale=None,
                        mid=None,
                        score=None,
                        confidence=None,
                        topicality=None,
                    ),
                    TextAnnotations(
                        text="YUGRA",
                        vertices=[
                            Vertices(x=457, y=296),
                            Vertices(x=513, y=296),
                            Vertices(x=513, y=307),
                            Vertices(x=457, y=307),
                        ],
                        locale=None,
                        mid=None,
                        score=None,
                        confidence=None,
                        topicality=None,
                    ),
                    TextAnnotations(
                        text="881",
                        vertices=[
                            Vertices(x=246, y=316),
                            Vertices(x=286, y=316),
                            Vertices(x=286, y=329),
                            Vertices(x=246, y=329),
                        ],
                        locale=None,
                        mid=None,
                        score=None,
                        confidence=None,
                        topicality=None,
                    ),
                    TextAnnotations(
                        text="CC1M",
                        vertices=[
                            Vertices(x=298, y=316),
                            Vertices(x=371, y=316),
                            Vertices(x=371, y=329),
                            Vertices(x=298, y=329),
                        ],
                        locale=None,
                        mid=None,
                        score=None,
                        confidence=None,
                        topicality=None,
                    ),
                ]
            ),
            {
                "name": ["САМВЕЛ", "ЮРЬЕВИЧ"],
                "patronymic": ["БАБАЯН"],
                "birthday": datetime.datetime(1980, 7, 1, 0, 0),
                "issue_date": datetime.datetime(2015, 9, 23, 0, 0),
                "expiration_date": datetime.datetime(2025, 9, 23, 0, 0),
                "code": 2322803756,
                "abode": ["ХАНТЫ", "-", "МАНСИЙСКИЙ", "АО", "-", "ЮГРА"],
            },
        ),
    ],
)
def test_driver_license_recognizer(
    document_recognizer: MockedSyncDocumentRecognition,
    driver_license_recognizer_by_template,
    response: ApiResponse,
    document_entity: Dict[str, Any],
) -> None:
    document_recognizer.add_result(response=response)
    document = document_recognizer.recognize_document(
        image_path="",
        recognizer=driver_license_recognizer_by_template,
    )
    assert isinstance(document, DriverLicense)
    assert document == dict_to_driver_license_with_sep(
        document_entity, driver_license_recognizer_by_template.separator
    )


@pytest.mark.parametrize(
    "response,expected_result",
    [  # TODO: move to file
        (
            ApiResponse(
                text="""
РОССИЙСКАЯ
отдел у МС РОССИИ ПО
КРАСНОДАРСКОМУ КРАЮ В ЛАБИНСКОМ Р-НЕ
28.01.2015
Bak
Kas ae
AS MATALMORRAR
MAY
pram
нь
ФЕДЕРАЦИЯ
024
муж
PAINE
230-024
Blu
ВИНИЧЕНКО
ДЕНИС
ВИТАЛЬЕВИЧ
25.12.1994
ГОР. ЛАБИНСК
КРАСНОДАРСКОГО КРАЯ
03 15 084752
03 15 084752
PNRUSVINIJENKO<<DENIS<VITAL9EVI3<<<<TTTTTTTL
0310847524RUS9412251M<<<<<<<5150128230024<32
""",
                text_annotations=[],
            ),
            Passport(
                serial_number="03 15",
                number="084752",
            ),
        )
    ],
)
def test_passport_recognizer_by_regex(
    passport_recognizer_by_regular_expression: PassportRecognizerByRegularExpression,
    response: ApiResponse,
    expected_result: Passport,
):
    passport = passport_recognizer_by_regular_expression(response=response)
    assert passport == expected_result
