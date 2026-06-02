#!/usr/bin/env python3
"""Generate SEASON campaign bar snippets for all locales."""

from pathlib import Path

BG = "#f1ecdf"
GREEN = "#8b927f"
BROWN = "#7a5b46"

LOCALES = {
    "es": {
        "comment": "ESPA&#209;A",
        "tag": "SEASON7",
        "pct": 7,
        "coupon": "SEASON7",
        "claim": "Tu centro listo para verano",
        "discount": "7% con el c&#243;digo",
        "hyva_discount": "7% CON EL C&#211;DIGO ",
        "mobile_word": "cup&#243;n",
        "cta_d": "VER PRODUCTOS",
        "cta_m": "VER PRODUCTOS",
        "url": "ofertas/ofertas-quirumed",
    },
    "pt": {
        "comment": "PORTUGAL",
        "tag": "SEASON7",
        "pct": 7,
        "coupon": "SEASON7",
        "claim": "O seu centro pronto para o ver&#227;o",
        "discount": "7% com o c&#243;digo",
        "hyva_discount": "7% COM O C&#211;DIGO ",
        "mobile_word": "cup&#227;o",
        "cta_d": "VER PRODUTOS",
        "cta_m": "VER PRODUTOS",
        "url": "ofertas/quirumed-ofertas",
    },
    "de": {
        "comment": "ALEMANIA",
        "tag": "SEASON5",
        "pct": 5,
        "coupon": "SEASON5",
        "claim": "Ihr Zentrum bereit f&#252;r den Sommer",
        "discount": "5% mit Code",
        "hyva_discount": "5% MIT CODE ",
        "mobile_word": "Code",
        "cta_d": "PRODUKTE ANSEHEN",
        "cta_m": "PRODUKTE",
        "url": "angebote/quirumed-blitzangebote",
    },
    "at": {
        "comment": "AUSTRIA",
        "tag": "SEASON5",
        "pct": 5,
        "coupon": "SEASON5",
        "claim": "Ihr Zentrum bereit f&#252;r den Sommer",
        "discount": "5% mit Code",
        "hyva_discount": "5% MIT CODE ",
        "mobile_word": "Code",
        "cta_d": "PRODUKTE ANSEHEN",
        "cta_m": "PRODUKTE",
        "url": "angebote/quirumed-aktionen",
    },
    "fr": {
        "comment": "FRANCIA",
        "tag": "SEASON5",
        "pct": 5,
        "coupon": "SEASON5",
        "claim": "Votre centre pr&#234;t pour l&#8217;&#233;t&#233;",
        "discount": "5% avec le code",
        "hyva_discount": "5% AVEC LE CODE ",
        "mobile_word": "code",
        "cta_d": "VOIR LES PRODUITS",
        "cta_m": "VOIR PRODUITS",
        "url": "offres/quirumed-promotions",
    },
    "be_fr": {
        "comment": "B&#201;LGICA FR",
        "tag": "SEASON5",
        "pct": 5,
        "coupon": "SEASON5",
        "claim": "Votre centre pr&#234;t pour l&#8217;&#233;t&#233;",
        "discount": "5% avec le code",
        "hyva_discount": "5% AVEC LE CODE ",
        "mobile_word": "code",
        "cta_d": "VOIR LES PRODUITS",
        "cta_m": "VOIR PRODUITS",
        "url": "offres/quirumed-promotions",
    },
    "be_nl": {
        "comment": "B&#201;LGICA NL",
        "tag": "SEASON5",
        "pct": 5,
        "coupon": "SEASON5",
        "claim": "Uw centrum klaar voor de zomer",
        "discount": "5% met code",
        "hyva_discount": "5% MET CODE ",
        "mobile_word": "code",
        "cta_d": "BEKIJK PRODUCTEN",
        "cta_m": "PRODUCTEN",
        "url": "aanbiedingen/quirumed-actie",
    },
    "nl": {
        "comment": "HOLANDA",
        "tag": "SEASON5",
        "pct": 5,
        "coupon": "SEASON5",
        "claim": "Uw centrum klaar voor de zomer",
        "discount": "5% met code",
        "hyva_discount": "5% MET CODE ",
        "mobile_word": "code",
        "cta_d": "BEKIJK PRODUCTEN",
        "cta_m": "PRODUCTEN",
        "url": "aanbiedingen/quirumed-deals",
    },
    "it": {
        "comment": "ITALIA",
        "tag": "SEASON5",
        "pct": 5,
        "coupon": "SEASON5",
        "claim": "Il tuo centro pronto per l&#8217;estate",
        "discount": "5% con codice",
        "hyva_discount": "5% CON CODICE ",
        "mobile_word": "codice",
        "cta_d": "VEDI PRODOTTI",
        "cta_m": "VEDI PRODOTTI",
        "url": "offerte/quirumed-promozioni",
    },
    "ch_de": {
        "comment": "SUIZA ALEM&#193;N",
        "tag": "SEASON5",
        "pct": 5,
        "coupon": "SEASON5",
        "claim": "Ihr Zentrum bereit f&#252;r den Sommer",
        "discount": "5% mit Code",
        "hyva_discount": "5% MIT CODE ",
        "mobile_word": "Code",
        "cta_d": "PRODUKTE ANSEHEN",
        "cta_m": "PRODUKTE",
        "url": "angebote/quirumed-sonderangebote",
    },
    "ch_fr": {
        "comment": "SUIZA FR",
        "tag": "SEASON5",
        "pct": 5,
        "coupon": "SEASON5",
        "claim": "Votre centre pr&#234;t pour l&#8217;&#233;t&#233;",
        "discount": "5% avec le code",
        "hyva_discount": "5% AVEC LE CODE ",
        "mobile_word": "code",
        "cta_d": "VOIR LES PRODUITS",
        "cta_m": "VOIR PRODUITS",
        "url": "offres/quirumed-offres-speciales",
    },
    "ch_it": {
        "comment": "SUIZA IT",
        "tag": "SEASON5",
        "pct": 5,
        "coupon": "SEASON5",
        "claim": "Il tuo centro pronto per l&#8217;estate",
        "discount": "5% con codice",
        "hyva_discount": "5% CON CODICE ",
        "mobile_word": "codice",
        "cta_d": "VEDI PRODOTTI",
        "cta_m": "VEDI PRODOTTI",
        "url": "offerte/quirumed-offerte-imperdibili",
    },
    "uk": {
        "comment": "REINO UNIDO",
        "tag": "SEASON5",
        "pct": 5,
        "coupon": "SEASON5",
        "claim": "Your centre ready for summer",
        "discount": "5% with code",
        "hyva_discount": "5% DISCOUNT CODE ",
        "mobile_word": "code",
        "cta_d": "VIEW PRODUCTS",
        "cta_m": "PRODUCTS",
        "url": "offers/quirumed-deals",
    },
    "ie": {
        "comment": "IRLANDA",
        "tag": "SEASON5",
        "pct": 5,
        "coupon": "SEASON5",
        "claim": "Your centre ready for summer",
        "discount": "5% with code",
        "hyva_discount": "5% WITH CODE ",
        "mobile_word": "code",
        "cta_d": "VIEW PRODUCTS",
        "cta_m": "PRODUCTS",
        "url": "offers/quirumed-offers",
    },
    "int_en": {
        "comment": "INTERNACIONAL",
        "tag": "SEASON5",
        "pct": 5,
        "coupon": "SEASON5",
        "claim": "Your centre ready for summer",
        "discount": "5% with code",
        "hyva_discount": "5% WITH CODE ",
        "mobile_word": "code",
        "cta_d": "VIEW PRODUCTS",
        "cta_m": "PRODUCTS",
        "url": "offers/quirumed-offers",
    },
    "gr": {
        "comment": "GRECIA",
        "tag": "SEASON5",
        "pct": 5,
        "coupon": "SEASON5",
        "claim": "&#932;&#959; &#954;&#941;&#957;&#964;&#961;&#959; &#963;&#945;&#962; &#941;&#964;&#959;&#953;&#956;&#959; &#947;&#953;&#945; &#964;&#959; &#954;&#945;&#955;&#959;&#954;&#945;&#943;&#961;&#953;",
        "discount": "5% &#956;&#949; &#954;&#969;&#948;&#953;&#954;&#972;",
        "hyva_discount": "5% &#924;&#917; &#922;&#937;&#916;&#921;&#922;&#927; ",
        "mobile_word": "&#954;&#969;&#948;.",
        "cta_d": "&#916;&#917;&#921;&#932;&#917; &#928;&#929;&#927;&#938;&#927;&#925;&#932;&#913;",
        "cta_m": "&#928;&#929;&#927;&#938;&#927;&#925;&#932;&#913;",
        "url": "prosfores/quirumed-prosfores",
    },
    "ro": {
        "comment": "RUMAN&#205;A",
        "tag": "SEASON5",
        "pct": 5,
        "coupon": "SEASON5",
        "claim": "Centrul dvs. preg&#259;tit pentru var&#259;",
        "discount": "5% cu codul",
        "hyva_discount": "5% CU CODUL ",
        "mobile_word": "cod",
        "cta_d": "VEZI PRODUSE",
        "cta_m": "VEZI PRODUSE",
        "url": "oferte/quirumed-oferte",
    },
    "pl": {
        "comment": "POLONIA",
        "tag": "SEASON5",
        "pct": 5,
        "coupon": "SEASON5",
        "claim": "Twoje centrum gotowe na lato",
        "discount": "5% z kodem",
        "hyva_discount": "5% Z KODEM ",
        "mobile_word": "kod",
        "cta_d": "ZOBACZ PRODUKTY",
        "cta_m": "PRODUKTY",
        "url": "oferty/quirumed-rabaty",
    },
    "cz": {
        "comment": "REP&#218;BLICA CHECA",
        "tag": "SEASON5",
        "pct": 5,
        "coupon": "SEASON5",
        "claim": "Va&#353;e centrum p&#345;ipraven&#233; na l&#233;to",
        "discount": "5% s k&#243;dem",
        "hyva_discount": "5% S K&#211;DEM ",
        "mobile_word": "k&#243;d",
        "cta_d": "ZOBRAZIT PRODUKTY",
        "cta_m": "PRODUKTY",
        "url": "nabidky/quirumed-nabidky",
    },
    "fi": {
        "comment": "FINLANDIA",
        "tag": "SEASON5",
        "pct": 5,
        "coupon": "SEASON5",
        "claim": "Keskuksesi valmiina kes&#228;&#228;n",
        "discount": "5% koodilla",
        "hyva_discount": "5% KOODILLA ",
        "mobile_word": "koodi",
        "cta_d": "KATSO TUOTTEET",
        "cta_m": "TUOTTEET",
        "url": "tarjoukset/quirumed-erikoistarjoukset",
    },
    "se": {
        "comment": "SUECIA",
        "tag": "SEASON5",
        "pct": 5,
        "coupon": "SEASON5",
        "claim": "Ert center redo f&#246;r sommaren",
        "discount": "5% med koden",
        "hyva_discount": "5% MED KODEN ",
        "mobile_word": "kod",
        "cta_d": "VISA PRODUKTER",
        "cta_m": "PRODUKTER",
        "url": "erbjudanden/quirumed-kampanjer",
    },
}

HYVA_LOCALES = ["nl", "gr", "ro", "uk", "ie", "int_en"]


def standard_html(cfg: dict) -> str:
    c = cfg
    pct = c["pct"]
    return f"""<!-- {c['comment']} - {c['tag']} - Desktop -->
<div class="extra-menu show-desktop" style="background-color:{BG};">
    <p style="margin:0; color:{BROWN}; font-size:16px;">
      <strong style="color:{GREEN};">{c['claim']}</strong> &#8211; {c['discount']}
      <strong style="background-color:{GREEN}; color:#FFFFFF; padding:2px 8px; border-radius:4px; font-family:monospace;">{c['coupon']}</strong>
      &nbsp;&#8211;&nbsp;
      <a href="{{{{store direct_url="{c['url']}"}}}}" style="color:{GREEN}; font-weight:bold; text-decoration:underline;">
        {c['cta_d']}
      </a>
    </p>
  </div>
  
  <!-- {c['comment']} - Mobile -->
  <div class="extra-menu show-mobile" style="background-color:{BG};">
    <p style="margin:0; font-size:12px; color:{BROWN};">
      <strong style="color:{GREEN};">{pct}%</strong> {c['mobile_word']} 
      <strong style="background-color:{GREEN}; color:#FFFFFF; padding:1px 5px; border-radius:3px; font-family:monospace;">{c['coupon']}</strong>
      &nbsp;|&nbsp;
      <a href="{{{{store direct_url="{c['url']}"}}}}" style="text-decoration:underline; color:{GREEN}; font-weight:bold;">
        {c['cta_m']}
      </a>
    </p>
  </div>
  
"""


def hyva_html(cfg: dict) -> str:
    c = cfg
    pct = c["pct"]
    return f"""<div class="hidden md:block text-center p-1"  style="background-color:{BG};">
    <p class="container" style="margin:0; color:{BROWN}; font-size:16px;"><b style="color:{GREEN};">{c['claim']}</b> <b style="color:{BROWN};">&#8211; {c['hyva_discount']}</b><strong style="background-color:{GREEN}; color:#FFFFFF; padding:2px 8px; border-radius:4px; font-family:monospace;">{c['coupon']}</strong><b style="color:{BROWN};"> | </b><span style="color:{BROWN};"> <a style="color:{GREEN};text-decoration:underline;" href="{{{{store direct_url="{c['url']}"}}}}"><span style="color:{GREEN}">{c['cta_d']}</span></a></span></p>
    </div>
    
    <div class="block md:hidden text-center p-1" style="background-color:{BG};">
    <p class="container"><a href="{{{{store direct_url="{c['url']}"}}}}"><span style="color:{BROWN};font-size:12px;">{pct}% {c['mobile_word']} </span><strong style="background-color:{GREEN}; color:#FFFFFF; padding:1px 5px; border-radius:3px; font-family:monospace;">{c['coupon']}</strong><span style="color:{BROWN};font-size:12px;"> | </span><span style="color:{BROWN};font-size:12px;">{c['cta_m']}</span></a></p>
    </div>
"""


def preview_section(tab_id: str, cfg: dict, hyva: bool = False) -> str:
    c = cfg
    pct = c["pct"]
    if hyva:
        return f"""  <div id="tab-{tab_id}" class="section">
    <div class="bar-wrapper">
      <div class="bar-desktop">
        <div class="bar-hyva-desktop">
          <b style="color:{GREEN};">{c['claim']}</b>
          <b style="color:{BROWN};"> &ndash; {c['hyva_discount'].rstrip()} </b>
          <strong style="background-color:{GREEN};color:#fff;padding:2px 8px;border-radius:4px;font-family:monospace;">{c['coupon']}</strong>
          <b style="color:{BROWN};"> | </b>
          <a href="#" style="color:{GREEN};text-decoration:underline;">{c['cta_d']}</a>
        </div>
      </div>
      <div class="bar-mobile">
        <div class="bar-hyva-mobile">
          <a href="#" style="color:{GREEN};text-decoration:none;">
            <span style="font-size:12px;color:{BROWN};">{pct}% {c['mobile_word']} </span>
            <strong style="background-color:{GREEN};color:#fff;padding:1px 5px;border-radius:3px;font-family:monospace;">{c['coupon']}</strong>
            <span style="font-size:12px;color:{BROWN};"> | </span>
            <span style="color:{BROWN};font-size:12px;">{c['cta_m']}</span>
          </a>
        </div>
      </div>
    </div>
  </div>
"""
    active = ' active' if tab_id == 'es' else ''
    return f"""  <div id="tab-{tab_id}" class="section{active}">
    <div class="bar-wrapper">
      <div class="bar-desktop">
        <strong class="label">{c['claim']}</strong> &ndash; {c['discount']}
        <span class="code">{c['coupon']}</span>
        &nbsp;&ndash;&nbsp;
        <a href="#">{c['cta_d']}</a>
      </div>
      <div class="bar-mobile">
        <strong>{pct}%</strong> {c['mobile_word']}
        <span class="code">{c['coupon']}</span>
        &nbsp;|&nbsp;
        <a href="#">{c['cta_m']}</a>
      </div>
    </div>
  </div>
"""


PREVIEW_TAB_ORDER = [
    "es",
    "pt",
    "de",
    "at",
    "fr",
    "be_fr",
    "be_nl",
    "nl",
    "nl_hyva",
    "it",
    "ch_de",
    "ch_fr",
    "ch_it",
    "uk",
    "uk_hyva",
    "ie",
    "ie_hyva",
    "int_en",
    "int_en_hyva",
    "gr",
    "gr_hyva",
    "ro",
    "ro_hyva",
    "pl",
    "cz",
    "fi",
    "se",
]


def update_preview_css(content: str) -> str:
    replacements = [
        ("#f4eae0", BG),
        ("#695240", BROWN),
    ]
    for old, new in replacements:
        content = content.replace(old, new)
    # Green accents in bar styles (after brown base replace)
    content = content.replace(
        ".bar-desktop strong.label { color: " + BROWN + "; }",
        ".bar-desktop strong.label { color: " + GREEN + "; }",
    )
    content = content.replace(
        ".bar-desktop .code {\n      background: " + BROWN + ";",
        ".bar-desktop .code {\n      background: " + GREEN + ";",
    )
    content = content.replace(
        ".bar-desktop a { color: " + BROWN + ";",
        ".bar-desktop a { color: " + GREEN + ";",
    )
    content = content.replace(
        ".bar-mobile strong { color: " + BROWN + "; }",
        ".bar-mobile strong { color: " + GREEN + "; }",
    )
    content = content.replace(
        ".bar-mobile .code {\n      background: " + BROWN + ";",
        ".bar-mobile .code {\n      background: " + GREEN + ";",
    )
    content = content.replace(
        ".bar-mobile a { color: " + BROWN + ";",
        ".bar-mobile a { color: " + GREEN + ";",
    )
    return content


def main() -> None:
    root = Path(__file__).resolve().parents[1]

    for locale, cfg in LOCALES.items():
        (root / f"{locale}.html").write_text(standard_html(cfg), encoding="utf-8")

    for locale in HYVA_LOCALES:
        (root / f"{locale}_hyva.html").write_text(hyva_html(LOCALES[locale]), encoding="utf-8")

    preview_path = root / "preview.html"
    preview = preview_path.read_text(encoding="utf-8")
    preview = update_preview_css(preview)

    start = preview.index('<div id="tab-es"')
    end = preview.index("</div>\n</main>")
    sections = []
    for tab in PREVIEW_TAB_ORDER:
        hyva = tab.endswith("_hyva")
        base = tab.replace("_hyva", "") if hyva else tab
        sections.append(preview_section(tab, LOCALES[base], hyva=hyva))

    preview = preview[:start] + "\n".join(sections) + "\n\n" + preview[end:]
    preview_path.write_text(preview, encoding="utf-8")
    print("Generated", len(LOCALES), "standard +", len(HYVA_LOCALES), "hyva + preview.html")


if __name__ == "__main__":
    main()
