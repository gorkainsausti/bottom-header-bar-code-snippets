#!/usr/bin/env python3
"""Generate QDAYS campaign bar snippets for all locales."""

from pathlib import Path

# Colores de campaña
STD_BG = "#83bb24"            # Fondo de los bloques estándar (no Hyvä)
HYVA_BG = "#2d54bb"           # Fondo de los bloques Hyvä
BROWN = "#ffffff"            # Color del texto principal
BADGE_BG = "#ffffff"         # Fondo del badge del cupón
STD_BADGE_TEXT = "#83bb24"   # Color del código del cupón en bloques estándar
HYVA_BADGE_TEXT = "#2d54bb"  # Color del código del cupón en bloques Hyvä
# Aliases de compatibilidad para las utilidades del preview
BG = STD_BG
GREEN = "#4f99f0"
BADGE_TEXT = HYVA_BADGE_TEXT
CLAIM = "Qdays!"

# Campaign end: 30/06 inclusive (23:59:59 local time)
COUNTDOWN_END = (2026, 5, 30, 23, 59, 59)  # month 0-indexed

LOCALES = {
    "es": {
        "comment": "ESPA&#209;A",
        "tag": "QDAYS8",
        "pct": 8,
        "coupon": "QDAYS8",
        "claim": CLAIM,
        "discount": "8% con el c&#243;digo",
        "hyva_discount": "8% CON EL C&#211;DIGO ",
        "mobile_word": "cup&#243;n",
        "ends_in": "Finaliza en:",
        "cta_d": "VER PRODUCTOS",
        "cta_m": "VER PRODUCTOS",
        "url": "ofertas/ofertas-quirumed",
    },
    "pt": {
        "comment": "PORTUGAL",
        "tag": "QDAYS8",
        "pct": 8,
        "coupon": "QDAYS8",
        "claim": CLAIM,
        "discount": "8% com o c&#243;digo",
        "hyva_discount": "8% COM O C&#211;DIGO ",
        "mobile_word": "cup&#227;o",
        "ends_in": "Termina em:",
        "cta_d": "VER PRODUTOS",
        "cta_m": "VER PRODUTOS",
        "url": "ofertas/quirumed-ofertas",
    },
    "de": {
        "comment": "ALEMANIA",
        "tag": "QDAYS6",
        "pct": 6,
        "coupon": "QDAYS6",
        "claim": CLAIM,
        "discount": "6% mit Code",
        "hyva_discount": "6% MIT CODE ",
        "mobile_word": "Code",
        "ends_in": "Endet in:",
        "cta_d": "PRODUKTE ANSEHEN",
        "cta_m": "PRODUKTE",
        "url": "angebote/quirumed-blitzangebote",
    },
    "at": {
        "comment": "AUSTRIA",
        "tag": "QDAYS6",
        "pct": 6,
        "coupon": "QDAYS6",
        "claim": CLAIM,
        "discount": "6% mit Code",
        "hyva_discount": "6% MIT CODE ",
        "mobile_word": "Code",
        "ends_in": "Endet in:",
        "cta_d": "PRODUKTE ANSEHEN",
        "cta_m": "PRODUKTE",
        "url": "angebote/quirumed-aktionen",
    },
    "fr": {
        "comment": "FRANCIA",
        "tag": "QDAYS6",
        "pct": 6,
        "coupon": "QDAYS6",
        "claim": CLAIM,
        "discount": "6% avec le code",
        "hyva_discount": "6% AVEC LE CODE ",
        "mobile_word": "code",
        "ends_in": "Se termine dans :",
        "cta_d": "VOIR LES PRODUITS",
        "cta_m": "VOIR PRODUITS",
        "url": "offres/quirumed-promotions",
    },
    "be_fr": {
        "comment": "B&#201;LGICA FR",
        "tag": "QDAYS6",
        "pct": 6,
        "coupon": "QDAYS6",
        "claim": CLAIM,
        "discount": "6% avec le code",
        "hyva_discount": "6% AVEC LE CODE ",
        "mobile_word": "code",
        "ends_in": "Se termine dans :",
        "cta_d": "VOIR LES PRODUITS",
        "cta_m": "VOIR PRODUITS",
        "url": "offres/quirumed-promotions",
    },
    "be_nl": {
        "comment": "B&#201;LGICA NL",
        "tag": "QDAYS6",
        "pct": 6,
        "coupon": "QDAYS6",
        "claim": CLAIM,
        "discount": "6% met code",
        "hyva_discount": "6% MET CODE ",
        "mobile_word": "code",
        "ends_in": "Eindigt over:",
        "cta_d": "BEKIJK PRODUCTEN",
        "cta_m": "PRODUCTEN",
        "url": "aanbiedingen/quirumed-actie",
    },
    "nl": {
        "comment": "HOLANDA",
        "tag": "QDAYS6",
        "pct": 6,
        "coupon": "QDAYS6",
        "claim": CLAIM,
        "discount": "6% met code",
        "hyva_discount": "6% MET CODE ",
        "mobile_word": "code",
        "ends_in": "Eindigt over:",
        "cta_d": "BEKIJK PRODUCTEN",
        "cta_m": "PRODUCTEN",
        "url": "aanbiedingen/quirumed-deals",
    },
    "it": {
        "comment": "ITALIA",
        "tag": "QDAYS6",
        "pct": 6,
        "coupon": "QDAYS6",
        "claim": CLAIM,
        "discount": "6% con codice",
        "hyva_discount": "6% CON CODICE ",
        "mobile_word": "codice",
        "ends_in": "Termina tra:",
        "cta_d": "VEDI PRODOTTI",
        "cta_m": "VEDI PRODOTTI",
        "url": "offerte/quirumed-promozioni",
    },
    "ch_de": {
        "comment": "SUIZA ALEM&#193;N",
        "tag": "QDAYS6",
        "pct": 6,
        "coupon": "QDAYS6",
        "claim": CLAIM,
        "discount": "6% mit Code",
        "hyva_discount": "6% MIT CODE ",
        "mobile_word": "Code",
        "ends_in": "Endet in:",
        "cta_d": "PRODUKTE ANSEHEN",
        "cta_m": "PRODUKTE",
        "url": "angebote/quirumed-sonderangebote",
    },
    "ch_fr": {
        "comment": "SUIZA FR",
        "tag": "QDAYS6",
        "pct": 6,
        "coupon": "QDAYS6",
        "claim": CLAIM,
        "discount": "6% avec le code",
        "hyva_discount": "6% AVEC LE CODE ",
        "mobile_word": "code",
        "ends_in": "Se termine dans :",
        "cta_d": "VOIR LES PRODUITS",
        "cta_m": "VOIR PRODUITS",
        "url": "offres/quirumed-offres-speciales",
    },
    "ch_it": {
        "comment": "SUIZA IT",
        "tag": "QDAYS6",
        "pct": 6,
        "coupon": "QDAYS6",
        "claim": CLAIM,
        "discount": "6% con codice",
        "hyva_discount": "6% CON CODICE ",
        "mobile_word": "codice",
        "ends_in": "Termina tra:",
        "cta_d": "VEDI PRODOTTI",
        "cta_m": "VEDI PRODOTTI",
        "url": "offerte/quirumed-offerte-imperdibili",
    },
    "uk": {
        "comment": "REINO UNIDO",
        "tag": "QDAYS6",
        "pct": 6,
        "coupon": "QDAYS6",
        "claim": CLAIM,
        "discount": "6% with code",
        "hyva_discount": "6% DISCOUNT CODE ",
        "mobile_word": "code",
        "ends_in": "Ends in:",
        "cta_d": "VIEW PRODUCTS",
        "cta_m": "PRODUCTS",
        "url": "offers/quirumed-deals",
    },
    "ie": {
        "comment": "IRLANDA",
        "tag": "QDAYS6",
        "pct": 6,
        "coupon": "QDAYS6",
        "claim": CLAIM,
        "discount": "6% with code",
        "hyva_discount": "6% DISCOUNT CODE ",
        "mobile_word": "code",
        "ends_in": "Ends in:",
        "cta_d": "VIEW PRODUCTS",
        "cta_m": "PRODUCTS",
        "url": "offers/quirumed-offers",
    },
    "int_en": {
        "comment": "INTERNACIONAL",
        "tag": "QDAYS6",
        "pct": 6,
        "coupon": "QDAYS6",
        "claim": CLAIM,
        "discount": "6% with code",
        "hyva_discount": "6% DISCOUNT CODE ",
        "mobile_word": "code",
        "ends_in": "Ends in:",
        "cta_d": "VIEW PRODUCTS",
        "cta_m": "PRODUCTS",
        "url": "offers/quirumed-offers",
    },
    "gr": {
        "comment": "GRECIA",
        "tag": "QDAYS6",
        "pct": 6,
        "coupon": "QDAYS6",
        "claim": CLAIM,
        "discount": "6% &#956;&#949; &#954;&#969;&#948;&#953;&#954;&#972;",
        "hyva_discount": "6% &#924;&#917; &#922;&#937;&#916;&#921;&#922;&#927; ",
        "mobile_word": "&#954;&#969;&#948;.",
        "ends_in": "&#923;&#942;&#947;&#949;&#953; &#963;&#949;:",
        "cta_d": "&#916;&#917;&#921;&#932;&#917; &#928;&#929;&#927;&#938;&#927;&#925;&#932;&#913;",
        "cta_m": "&#928;&#929;&#927;&#938;&#927;&#925;&#932;&#913;",
        "url": "prosfores/quirumed-prosfores",
    },
    "ro": {
        "comment": "RUMAN&#205;A",
        "tag": "QDAYS6",
        "pct": 6,
        "coupon": "QDAYS6",
        "claim": CLAIM,
        "discount": "6% cu codul",
        "hyva_discount": "6% CU CODUL ",
        "mobile_word": "cod",
        "ends_in": "Se termin&#259; &#238;n:",
        "cta_d": "VEZI PRODUSE",
        "cta_m": "VEZI PRODUSE",
        "url": "oferte/quirumed-oferte",
    },
    "pl": {
        "comment": "POLONIA",
        "tag": "QDAYS6",
        "pct": 6,
        "coupon": "QDAYS6",
        "claim": CLAIM,
        "discount": "6% z kodem",
        "hyva_discount": "6% Z KODEM ",
        "mobile_word": "kod",
        "ends_in": "Ko&#324;czy si&#281; za:",
        "cta_d": "ZOBACZ PRODUKTY",
        "cta_m": "PRODUKTY",
        "url": "oferty/quirumed-rabaty",
    },
    "cz": {
        "comment": "REP&#218;BLICA CHECA",
        "tag": "QDAYS6",
        "pct": 6,
        "coupon": "QDAYS6",
        "claim": CLAIM,
        "discount": "6% s k&#243;dem",
        "hyva_discount": "6% S K&#211;DEM ",
        "mobile_word": "k&#243;d",
        "ends_in": "Kon&#269;&#237; za:",
        "cta_d": "ZOBRAZIT PRODUKTY",
        "cta_m": "PRODUKTY",
        "url": "nabidky/quirumed-nabidky",
    },
    "fi": {
        "comment": "FINLANDIA",
        "tag": "QDAYS6",
        "pct": 6,
        "coupon": "QDAYS6",
        "claim": CLAIM,
        "discount": "6% koodilla",
        "hyva_discount": "6% KOODILLA ",
        "mobile_word": "koodi",
        "ends_in": "P&#228;&#228;ttyy:",
        "cta_d": "KATSO TUOTTEET",
        "cta_m": "TUOTTEET",
        "url": "tarjoukset/quirumed-erikoistarjoukset",
    },
    "se": {
        "comment": "SUECIA",
        "tag": "QDAYS6",
        "pct": 6,
        "coupon": "QDAYS6",
        "claim": CLAIM,
        "discount": "6% med koden",
        "hyva_discount": "6% MED KODEN ",
        "mobile_word": "kod",
        "ends_in": "Slutar om:",
        "cta_d": "VISA PRODUKTER",
        "cta_m": "PRODUKTER",
        "url": "erbjudanden/quirumed-kampanjer",
    },
}

HYVA_LOCALES = [
    "nl",
    "gr",
    "ro",
    "uk",
    "ie",
    "int_en",
    "at",
    "fi",
    "be_nl",
    "be_fr",
]

COUNTDOWN_CLASS = "qdays-cd-timer"
COUNTDOWN_SCRIPT = f"""<script>
(function() {{
  var end = new Date({COUNTDOWN_END[0]}, {COUNTDOWN_END[1]}, {COUNTDOWN_END[2]}, {COUNTDOWN_END[3]}, {COUNTDOWN_END[4]}, {COUNTDOWN_END[5]});
  function tick() {{
    var diff = end - Date.now();
    if (diff < 0) diff = 0;
    var sec = Math.floor(diff / 1000);
    var days = Math.floor(sec / 86400); sec %= 86400;
    var hrs = Math.floor(sec / 3600); sec %= 3600;
    var mins = Math.floor(sec / 60); sec %= 60;
    var text = days + "d " + hrs + "h " + mins + "m " + sec + "s";
    document.querySelectorAll(".{COUNTDOWN_CLASS}").forEach(function(el) {{
      el.textContent = text;
    }});
  }}
  tick();
  setInterval(tick, 1000);
}})();
</script>
"""


def countdown_inline(cfg: dict) -> str:
    # color en cada nodo de texto para evitar conflictos de CSS de la web (el countdown salía en rojo)
    return (
        f'<span style="color:{BROWN} !important;">&nbsp;|&nbsp;</span> <span style="color:{BROWN} !important;">{cfg["ends_in"]}</span>&nbsp;'
        f'<span class="{COUNTDOWN_CLASS}" style="color:{BROWN} !important;font-variant-numeric:tabular-nums;"></span>'
    )


def countdown_mobile_block(cfg: dict) -> str:
    # color en cada nodo de texto para evitar conflictos de CSS de la web (el countdown salía en rojo)
    return (
        f'<span style="display:block;color:{BROWN} !important;">{cfg["ends_in"]}&nbsp;'
        f'<span class="{COUNTDOWN_CLASS}" style="color:{BROWN} !important;font-variant-numeric:tabular-nums;"></span></span>'
    )


def standard_html(cfg: dict, countdown: bool = False) -> str:
    c = cfg
    pct = c["pct"]
    cd_desktop = countdown_inline(c) if countdown else ""
    suffix = f"\n{COUNTDOWN_SCRIPT}" if countdown else ""
    if countdown:
        mobile_block = f"""  <!-- {c['comment']} - Mobile -->
  <div class="extra-menu show-mobile" style="background-color:{STD_BG};">
    <p style="margin:0; font-size:12px; color:{BROWN} !important; text-align:center; line-height:1.35;">
      <span style="display:block;color:{BROWN} !important;">
      <strong style="color:{BROWN} !important;">{pct}%</strong> <span style="color:{BROWN} !important;">{c['mobile_word']}</span> 
      <strong style="background-color:{BADGE_BG}; color:{STD_BADGE_TEXT} !important; padding:1px 5px; border-radius:3px; font-family:monospace;">{c['coupon']}</strong>
      <span style="color:{BROWN} !important;">&nbsp;|&nbsp;</span>
      <a href="{{{{store direct_url="{c['url']}"}}}}" style="text-decoration:underline; color:{BROWN} !important; font-weight:bold;">
        {c['cta_m']}
      </a>
    </span>
      {countdown_mobile_block(c)}
    </p>
  </div>
  {suffix}
"""
    else:
        mobile_block = f"""  <!-- {c['comment']} - Mobile -->
  <div class="extra-menu show-mobile" style="background-color:{STD_BG};">
    <p style="margin:0; font-size:12px; color:{BROWN} !important;">
      <strong style="color:{BROWN} !important;">{pct}%</strong> <span style="color:{BROWN} !important;">{c['mobile_word']}</span> 
      <strong style="background-color:{BADGE_BG}; color:{STD_BADGE_TEXT} !important; padding:1px 5px; border-radius:3px; font-family:monospace;">{c['coupon']}</strong>
      <span style="color:{BROWN} !important;">&nbsp;|&nbsp;</span>
      <a href="{{{{store direct_url="{c['url']}"}}}}" style="text-decoration:underline; color:{BROWN} !important; font-weight:bold;">
        {c['cta_m']}
      </a>
    </p>
  </div>
  
"""
    return f"""<!-- {c['comment']} - {c['tag']}{' - Countdown' if countdown else ''} - Desktop -->
<div class="extra-menu show-desktop" style="background-color:{STD_BG};">
    <p style="margin:0; color:{BROWN} !important; font-size:16px;">
      <strong style="color:{BROWN} !important;">{c['claim']}</strong> <span style="color:{BROWN} !important;">&#8211; {c['discount']}</span>
      <strong style="background-color:{BADGE_BG}; color:{STD_BADGE_TEXT} !important; padding:2px 8px; border-radius:4px; font-family:monospace;">{c['coupon']}</strong>
      <span style="color:{BROWN} !important;">&nbsp;&#8211;&nbsp;</span>
      <a href="{{{{store direct_url="{c['url']}"}}}}" style="color:{BROWN} !important; font-weight:bold; text-decoration:underline;">
        {c['cta_d']}
      </a>{cd_desktop}
    </p>
  </div>
  
{mobile_block}"""


def hyva_html(cfg: dict, countdown: bool = False) -> str:
    c = cfg
    pct = c["pct"]
    cd_desktop = countdown_inline(c) if countdown else ""
    suffix = f"\n{COUNTDOWN_SCRIPT}" if countdown else ""
    if countdown:
        mobile_block = f"""    <div class="block md:hidden text-center p-1" style="background-color:{HYVA_BG};">
    <p class="container" style="margin:0; line-height:1.35;"><a href="{{{{store direct_url="{c['url']}"}}}}" style="text-decoration:none;"><span style="display:block;"><span style="color:{BROWN} !important;font-size:12px;">{c['hyva_discount']}</span><strong style="background-color:{BADGE_BG}; color:{HYVA_BADGE_TEXT} !important; padding:1px 5px; border-radius:3px; font-family:monospace;">{c['coupon']}</strong><span style="color:{BROWN} !important;font-size:12px;"> | </span><span style="color:{BROWN} !important;font-size:12px;text-decoration:underline;">{c['cta_d']}</span></span><span style="display:block;color:{BROWN} !important;font-size:12px;">{c['ends_in']}&nbsp;<span class="{COUNTDOWN_CLASS}" style="color:{BROWN} !important;font-variant-numeric:tabular-nums;"></span></span></a></p>
    </div>
{suffix}"""
    else:
        mobile_block = f"""    <div class="block md:hidden text-center p-1" style="background-color:{HYVA_BG};">
    <p class="container"><a href="{{{{store direct_url="{c['url']}"}}}}" style="text-decoration:none;"><span style="color:{BROWN} !important;font-size:12px;">{c['hyva_discount']}</span><strong style="background-color:{BADGE_BG}; color:{HYVA_BADGE_TEXT} !important; padding:1px 5px; border-radius:3px; font-family:monospace;">{c['coupon']}</strong><span style="color:{BROWN} !important;font-size:12px;"> | </span><span style="color:{BROWN} !important;font-size:12px;text-decoration:underline;">{c['cta_d']}</span></a></p>
    </div>
"""
    return f"""<div class="hidden md:block text-center p-1"  style="background-color:{HYVA_BG};">
    <p class="container" style="margin:0; color:{BROWN} !important; font-size:16px;"><b style="color:{BROWN} !important;">{c['claim']}</b> <b style="color:{BROWN} !important;">&#8211; {c['hyva_discount']}</b><strong style="background-color:{BADGE_BG}; color:{HYVA_BADGE_TEXT} !important; padding:2px 8px; border-radius:4px; font-family:monospace;">{c['coupon']}</strong><b style="color:{BROWN} !important;"> | </b><span style="color:{BROWN} !important;"> <a style="color:{BROWN} !important;text-decoration:underline;" href="{{{{store direct_url="{c['url']}"}}}}"><span style="color:{BROWN} !important;">{c['cta_d']}</span></a></span>{cd_desktop}</p>
    </div>
    
{mobile_block}"""


def preview_section(tab_id: str, cfg: dict, hyva: bool = False, countdown: bool = False) -> str:
    c = cfg
    pct = c["pct"]
    cd_id = f"preview-cd-{tab_id}"
    cd = ""
    if countdown:
        cd = (
            f' &nbsp;|&nbsp; {c["ends_in"]}&nbsp;'
            f'<span id="{cd_id}" class="countdown" style="font-variant-numeric:tabular-nums;"></span>'
        )
    cd_mobile = ""
    if countdown:
        cd_mobile = (
            f'<span class="countdown-line">{c["ends_in"]}&nbsp;'
            f'<span id="{cd_id}-m" class="countdown" style="font-variant-numeric:tabular-nums;"></span></span>'
        )
    if hyva:
        return f"""  <div id="tab-{tab_id}" class="section">
    <div class="bar-wrapper">
      <div class="bar-desktop">
        <div class="bar-hyva-desktop">
          <b style="color:{BROWN} !important;">{c['claim']}</b>
          <b style="color:{BROWN};"> &ndash; {c['hyva_discount'].rstrip()} </b>
          <strong style="background-color:{BADGE_BG};color:{HYVA_BADGE_TEXT};padding:2px 8px;border-radius:4px;font-family:monospace;">{c['coupon']}</strong>
          <b style="color:{BROWN};"> | </b>
          <a href="#" style="color:{BROWN} !important;text-decoration:underline;">{c['cta_d']}</a>{cd}
        </div>
      </div>
      <div class="bar-mobile">
        <div class="bar-hyva-mobile">
          <a href="#" style="color:{BROWN};text-decoration:none;">
            <span style="display:block;">
              <span style="font-size:12px;color:{BROWN};">{c['hyva_discount']}</span>
              <strong style="background-color:{BADGE_BG};color:{HYVA_BADGE_TEXT};padding:1px 5px;border-radius:3px;font-family:monospace;">{c['coupon']}</strong>
              <span style="font-size:12px;color:{BROWN};"> | </span>
              <span style="color:{BROWN};font-size:12px;text-decoration:underline;">{c['cta_d']}</span>
            </span>
            {cd_mobile}
          </a>
        </div>
      </div>
    </div>
  </div>
"""
    active = " active" if tab_id == "es" else ""
    return f"""  <div id="tab-{tab_id}" class="section{active}">
    <div class="bar-wrapper">
      <div class="bar-desktop">
        <strong class="label">{c['claim']}</strong> &ndash; {c['discount']}
        <span class="code">{c['coupon']}</span>
        &nbsp;&ndash;&nbsp;
        <a href="#">{c['cta_d']}</a>{cd}
      </div>
      <div class="bar-mobile">
        <span style="display:block;">
          <strong>{pct}%</strong> {c['mobile_word']}
          <span class="code">{c['coupon']}</span>
          &nbsp;|&nbsp;
          <a href="#">{c['cta_m']}</a>
        </span>
        {cd_mobile}
      </div>
    </div>
  </div>
"""


PREVIEW_TAB_ORDER = [
    "es",
    "es_countdown",
    "pt",
    "pt_countdown",
    "de",
    "de_countdown",
    "at",
    "at_hyva",
    "at_hyva_countdown",
    "fr",
    "fr_countdown",
    "be_fr",
    "be_fr_hyva",
    "be_fr_hyva_countdown",
    "be_nl",
    "be_nl_hyva",
    "be_nl_hyva_countdown",
    "nl",
    "nl_hyva",
    "nl_hyva_countdown",
    "it",
    "it_countdown",
    "ch_de",
    "ch_de_countdown",
    "ch_fr",
    "ch_fr_countdown",
    "ch_it",
    "ch_it_countdown",
    "uk",
    "uk_hyva",
    "uk_hyva_countdown",
    "ie",
    "ie_hyva",
    "ie_hyva_countdown",
    "int_en",
    "int_en_hyva",
    "int_en_hyva_countdown",
    "gr",
    "gr_hyva",
    "gr_hyva_countdown",
    "ro",
    "ro_hyva",
    "ro_hyva_countdown",
    "pl",
    "pl_countdown",
    "cz",
    "cz_countdown",
    "fi",
    "fi_hyva",
    "fi_hyva_countdown",
    "se",
    "se_countdown",
]

PREVIEW_COUNTDOWN_SCRIPT = """
  (function () {
    var end = new Date(2026, 5, 30, 23, 59, 59);
    function fmt(diff) {
      if (diff < 0) diff = 0;
      var s = Math.floor(diff / 1000);
      var d = Math.floor(s / 86400); s %= 86400;
      var h = Math.floor(s / 3600); s %= 3600;
      var m = Math.floor(s / 60); s %= 60;
      return d + 'd ' + h + 'h ' + m + 'm ' + s + 's';
    }
    function tick() {
      var now = Date.now();
      var text = fmt(end - now);
      document.querySelectorAll('.countdown').forEach(function (el) {
        el.textContent = text;
      });
    }
    tick();
    setInterval(tick, 1000);
  })();
"""


def preview_tab_label(tab: str) -> str:
    labels = {
        "es": "ES",
        "pt": "PT",
        "de": "DE",
        "at": "AT",
        "fr": "FR",
        "be_fr": "BE-FR",
        "be_nl": "BE-NL",
        "nl": "NL",
        "it": "IT",
        "ch_de": "CH-DE",
        "ch_fr": "CH-FR",
        "ch_it": "CH-IT",
        "uk": "UK",
        "ie": "IE",
        "int_en": "INT",
        "gr": "GR",
        "ro": "RO",
        "pl": "PL",
        "cz": "CZ",
        "fi": "FI",
        "se": "SE",
    }
    if tab.endswith("_hyva_countdown"):
        base = tab.replace("_hyva_countdown", "")
        return f"{labels.get(base, base.upper())} Hyva CD"
    if tab.endswith("_countdown"):
        base = tab.replace("_countdown", "")
        return f"{labels.get(base, base.upper())} CD"
    if tab.endswith("_hyva"):
        base = tab.replace("_hyva", "")
        return f"{labels.get(base, base.upper())} Hyva"
    return labels.get(tab, tab.upper())


def parse_preview_tab(tab: str) -> tuple[str, bool, bool]:
    countdown = tab.endswith("_countdown") or tab.endswith("_hyva_countdown")
    hyva = "_hyva" in tab
    base = tab
    if tab.endswith("_hyva_countdown"):
        base = tab.replace("_hyva_countdown", "")
    elif tab.endswith("_countdown"):
        base = tab.replace("_countdown", "")
    elif tab.endswith("_hyva"):
        base = tab.replace("_hyva", "")
    return base, hyva, countdown


def update_preview_css(content: str) -> str:
    content = content.replace(
        "background: #ffffff; color: #81a4c9;",
        f"background: {BADGE_BG}; color: {BADGE_TEXT};",
    )
    for old_bg in ("#81a4c9", "#f1ecdf", "#f4eae0"):
        content = content.replace(old_bg, BG)
    for old_text in ("#7a5b46", "#695240"):
        content = content.replace(old_text, BROWN)
    content = content.replace("#8b927f", BROWN)
    content = content.replace("#4f99f0", BROWN)
    for old_hint in (
        "SUMMER7 ES/PT · SUMMER5 resto · 3/6–16/6",
        "QDAYS8 ES/PT · QDAYS6 resto · 23/6–30/6",
    ):
        content = content.replace(old_hint, "QDAYS8 ES/PT · QDAYS6 resto · 23/6–30/6")
    if ".bar-hyva-desktop a" not in content:
        content = content.replace(
            "    .bar-hyva-desktop {",
            "    .bar-hyva-desktop b,\n"
            "    .bar-hyva-desktop a,\n"
            "    .bar-hyva-desktop a span,\n"
            "    .bar-hyva-mobile a,\n"
            "    .bar-hyva-mobile span { color: #ffffff !important; }\n\n"
            "    .countdown-line { display: block; margin-top: 2px; }\n\n"
            "    .bar-hyva-desktop {",
        )
    return content


def rebuild_preview_nav(content: str) -> str:
    start = content.index('<nav class="locales"')
    end = content.index("</nav>", start)
    buttons = []
    for tab in PREVIEW_TAB_ORDER:
        active = ' class="active"' if tab == "es" else ""
        label = preview_tab_label(tab)
        buttons.append(f'    <button type="button"{active} data-tab="{tab}">{label}</button>')
    nav = '<nav class="locales" aria-label="Locales">\n' + "\n".join(buttons) + "\n  </nav>"
    return content[:start] + nav + content[end + len("</nav>") :]


def inject_preview_countdown(content: str) -> str:
    marker = "</script>\n</body>"
    if PREVIEW_COUNTDOWN_SCRIPT.strip() in content:
        return content
    return content.replace(marker, PREVIEW_COUNTDOWN_SCRIPT + marker)


def main() -> None:
    root = Path(__file__).resolve().parents[1]

    for locale, cfg in LOCALES.items():
        (root / f"{locale}.html").write_text(standard_html(cfg), encoding="utf-8")
        (root / f"{locale}_countdown.html").write_text(
            standard_html(cfg, countdown=True), encoding="utf-8"
        )

    for locale in HYVA_LOCALES:
        cfg = LOCALES[locale]
        (root / f"{locale}_hyva.html").write_text(hyva_html(cfg), encoding="utf-8")
        (root / f"{locale}_hyva_countdown.html").write_text(
            hyva_html(cfg, countdown=True), encoding="utf-8"
        )

    preview_path = root / "preview.html"
    preview = preview_path.read_text(encoding="utf-8")
    preview = update_preview_css(preview)
    preview = rebuild_preview_nav(preview)

    start = preview.index('<div id="tab-es"')
    end = preview.index("</div>\n</main>")
    sections = []
    for tab in PREVIEW_TAB_ORDER:
        base, hyva, countdown = parse_preview_tab(tab)
        sections.append(preview_section(tab, LOCALES[base], hyva=hyva, countdown=countdown))

    preview = preview[:start] + "\n".join(sections) + "\n\n" + preview[end:]
    preview = inject_preview_countdown(preview)
    preview_path.write_text(preview, encoding="utf-8")

    total_countdown = len(LOCALES) + len(HYVA_LOCALES)
    print(
        "Generated",
        len(LOCALES),
        "standard +",
        len(HYVA_LOCALES),
        "hyva +",
        total_countdown,
        "countdown + preview.html",
    )


if __name__ == "__main__":
    main()
