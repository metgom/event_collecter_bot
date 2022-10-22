from typing import Final

"""
이벤트 종류
로그인
로그아웃
상품 메인화면 진입
상품 상세페이지 진입
상품 구매 진입
상품 구매 성공
상품 구매 실패 - 인증 실패, 기타 오류 등으로 인한 구매 실패
"""
EVENT_NONE:     Final = -1
EVENT_LOGIN:    Final = 0
EVENT_LOGOUT:   Final = 1
EVENT_PRODUCTS:         Final = 2
EVENT_PRODUCT_DETAILS:  Final = 3
EVENT_PURCHASE:         Final = 4
EVENT_PURCHASE_SUCCESS: Final = 5
EVENT_PURCHASE_FAIL:    Final = 6
EVENT_END:    Final = 7

_EVENT_NAME = ["log_in",
               "log_out",
               "products_main",
               "product_details",
               "purchase",
               "purchase_success",
               "purchase_fail"]


def get_event_name(flag: int):
    if flag <= EVENT_NONE or flag >= EVENT_END:
        return "none"
    return _EVENT_NAME[flag]
