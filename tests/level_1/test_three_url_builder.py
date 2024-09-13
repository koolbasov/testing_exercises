from functions.level_1.three_url_builder import build_url


def test_build_url():
    assert build_url("ya.ru", "search", {"text": "docker", "lr": 2}) == "ya.ru/search?text=docker&lr=2"
    assert build_url("ya.ru", "search", {"text": "милые+котики", "lr": 2}) == "ya.ru/search?text=милые+котики&lr=2"
    assert (
        build_url(
            "ya.ru",
            "maps/2/saint-petersburg/geo/nevskiy_prospekt/8019294",
            {"ll": "30.349012%2C59.930532", "source": "serp_navig", "z": 14},
        )
        == "ya.ru/maps/2/saint-petersburg/geo/nevskiy_prospekt/8019294?ll=30.349012%2C59.930532&source=serp_navig&z=14"
    )
