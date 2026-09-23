"""Erzeugt das Anki-Deck „Darija – Feilschen & Alltag“ als .apkg und .txt.

Aufruf:  pip install genanki && python3 build_deck.py
"""
import genanki

# (Deutsch, Darija-Umschrift, Arabisch, Hinweis, Tag)
VOCAB = [
    # 1. Begrüßung & Höflichkeit
    ("Hallo (Friede sei mit dir)", "Salam ʿalikum / Salam", "السلام عليكم", "Immer zuerst grüßen, dann nach dem Preis fragen", "begruessung"),
    ("Antwort auf den Gruß", "Wa ʿalikum salam", "وعليكم السلام", "", "begruessung"),
    ("Wie geht's? / Alles gut?", "Labas?", "لاباس؟", "Direkt nach Salam", "begruessung"),
    ("Gut, Gott sei Dank", "Labas, l-ḥamdulillah", "لاباس، الحمد لله", "Standardantwort", "begruessung"),
    ("Danke", "Schukran", "شكرا", "", "begruessung"),
    ("Vielen Dank", "Schukran bzzaf", "شكرا بزاف", "bzzaf = viel / sehr", "begruessung"),
    ("Bitte (bei einer Bitte)", "ʿAfak", "عافاك", "ʿ = Kehllaut (Arabizi 3)", "begruessung"),
    ("Nein danke", "La, schukran", "لا، شكرا", "Höfliche Absage an Händler und Schlepper", "begruessung"),
    ("Tschüss / Auf Wiedersehen", "Bslama", "بسلامة", "", "begruessung"),
    ("So Gott will / vielleicht", "Inschallah", "إن شاء الله", "Oft auch „mal sehen“", "begruessung"),
    ("Entschuldigung", "Smeḥ li", "سمح لي", "Auch „darf ich vorbei?“", "begruessung"),
    ("Gott segne dich (herzlicher Dank)", "Barak llahu fik", "بارك الله فيك", "Wärmer als schukran", "begruessung"),
    ("Gott möge es dir leicht machen (höfliche Absage)", "Allah ysahel", "الله يسهل", "An Bettler / aufdringliche Verkäufer, dann weitergehen", "begruessung"),
    ("Kein Problem", "Ma kayn mschkil", "ماكاين مشكل", "", "begruessung"),
    ("Ich verstehe nicht", "Ma fhemtsch", "ما فهمتش", "", "begruessung"),
    ("Langsam bitte", "B schwiya ʿafak", "بشوية عافاك", "Wenn Zahlen zu schnell kommen", "begruessung"),

    # 2. Verhandeln
    ("Wie viel?", "Bschḥal?", "بشحال؟", "ḥ = scharfes h (Arabizi 7)", "verhandeln"),
    ("Wie viel kostet das? (m.)", "Bschḥal hada?", "بشحال هادا؟", "", "verhandeln"),
    ("Wie viel kostet das? (f.)", "Bschḥal hadi?", "بشحال هادي؟", "Für feminine Dinge, z. B. jellaba", "verhandeln"),
    ("Was ist das?", "Schnu hada?", "شنو هادا؟", "", "verhandeln"),
    ("teuer", "ghali", "غالي", "gh = Zäpfchen-r", "verhandeln"),
    ("Zu teuer!", "Ghali bzzaf!", "غالي بزاف", "Mit einem Lächeln sagen", "verhandeln"),
    ("Das ist viel!", "Bzzaf! / Hadschi bzzaf", "هادشي بزاف", "Reaktion auf den ersten Preis", "verhandeln"),
    ("billig", "rkhiṣ", "رخيص", "kh = ch wie in „Bach“", "verhandeln"),
    ("Gibt es etwas Billigeres?", "Kayn schi ḥaja rkhiṣa?", "كاين شي حاجة رخيصة؟", "", "verhandeln"),
    ("Geh ein bisschen runter (mit dem Preis), bitte", "Nqeṣ schwiya ʿafak", "نقص شوية عافاك", "Freundlicher Standardsatz", "verhandeln"),
    ("Kannst du runtergehen?", "Momkin tnqeṣ?", "ممكن تنقص؟", "Höflicher, wenn der Preis fast passt", "verhandeln"),
    ("Mach mir einen guten Preis", "Dir mʿaya schi taman mzyan", "دير معايا شي ثمن مزيان", "", "verhandeln"),
    ("Ich gebe dir …", "Gha nʿṭik …", "غادي نعطيك …", "Leitet dein Gegenangebot ein", "verhandeln"),
    ("Ich gebe dir 100 Dirham dafür", "Nʿṭik fiha mya derhem", "نعطيك فيها مية درهم", "", "verhandeln"),
    ("Letzter Preis?", "Akhir taman?", "آخر ثمن؟", "Erst gegen Ende benutzen", "verhandeln"),
    ("Das ist mein letzter Preis", "Hada akhir taman", "هادا آخر ثمن", "", "verhandeln"),
    ("ein bisschen", "schwiya", "شوية", "", "verhandeln"),
    ("Sehr schön, aber teuer", "Zwin bzzaf, walakin ghali", "زوين بزاف، ولكن غالي", "Erst loben, dann verhandeln", "verhandeln"),
    ("Ist das Handarbeit?", "Hada dyal l-yed?", "هادا ديال اليد؟", "Zeigt Sinn für Qualität", "verhandeln"),
    ("Ich schaue nur", "Ghir kanschuf", "غير كنشوف", "Gegen „Komm rein, nur schauen!“", "verhandeln"),
    ("Ich möchte … / Ich will …", "Bghit …", "بغيت …", "Bghit hada = Ich will das", "verhandeln"),
    ("Ich will nicht", "Ma bghitsch", "ما بغيتش", "", "verhandeln"),
    ("Okay / Einverstanden", "Wakha", "واخا", "Das universelle „okay“", "verhandeln"),
    ("Fertig / Deal / Das war's", "Safi", "صافي", "Auch: genug", "verhandeln"),
    ("Genug! / Stopp!", "Baraka!", "باركا", "", "verhandeln"),
    ("Ja", "Iyyeh", "إيه", "", "verhandeln"),
    ("Nein", "La", "لا", "", "verhandeln"),
    ("Ich nehme es", "Ghadi ndih (m.) / ndiha (f.)", "غادي نديه / نديها", "Abschluss", "verhandeln"),
    ("Ich überlege es mir", "Ghadi nfekker", "غادي نفكر", "Eleganter Ausstieg", "verhandeln"),
    ("Ich schaue mich um und komme wieder", "Ghadi ndur w nrjeʿ", "غادي ندور ونرجع", "Wer weggeht, bekommt oft ein neues Angebot", "verhandeln"),
    ("Ich habe nicht viel Geld", "Ma ʿndisch bzzaf d l-flus", "ما عنديش بزاف د الفلوس", "", "verhandeln"),
    ("Rial oder Dirham?", "Wasch ryal wla derhem?", "واش ريال ولا درهم؟", "Fragen, wenn eine Zahl absurd hoch klingt", "verhandeln"),
    ("(Verkäufer:) Deal – Gott gebe Gewinn", "Allah yrbbeḥ", "الله يربح", "Hört man beim Abschluss – nicht als Absage benutzen", "verhandeln"),

    # 3. Zahlen
    ("1", "waḥed", "واحد", "", "zahlen"),
    ("2", "jouj", "جوج", "In 22, 32 …: tnayn (tnayn w rebʿin = 42)", "zahlen"),
    ("3", "tlata", "تلاتة", "", "zahlen"),
    ("4", "rebʿa", "ربعة", "", "zahlen"),
    ("5", "khamsa", "خمسة", "", "zahlen"),
    ("6", "setta", "ستة", "", "zahlen"),
    ("7", "sebʿa", "سبعة", "", "zahlen"),
    ("8", "tmenya", "تمنية", "", "zahlen"),
    ("9", "tesʿud", "تسعود", "", "zahlen"),
    ("10", "ʿaschra", "عشرة", "", "zahlen"),
    ("11", "ḥdasch", "حضاش", "11–19 enden auf -tasch / -asch", "zahlen"),
    ("12", "ṭnasch", "طناش", "", "zahlen"),
    ("20", "ʿeschrin", "عشرين", "", "zahlen"),
    ("25", "khamsa w ʿeschrin", "خمسة وعشرين", "Einer vor Zehner – wie im Deutschen", "zahlen"),
    ("30", "tlatin", "تلاتين", "", "zahlen"),
    ("40", "rebʿin", "ربعين", "", "zahlen"),
    ("50", "khamsin", "خمسين", "", "zahlen"),
    ("60", "settin", "ستين", "", "zahlen"),
    ("70", "sebʿin", "سبعين", "", "zahlen"),
    ("80", "tmanin", "تمانين", "", "zahlen"),
    ("90", "tesʿin", "تسعين", "", "zahlen"),
    ("100", "mya", "مية", "100 DH = myat derhem", "zahlen"),
    ("150", "mya w khamsin", "مية وخمسين", "", "zahlen"),
    ("200", "myatayn", "ميتين", "", "zahlen"),
    ("300", "teltmya", "تلتمية", "", "zahlen"),
    ("500", "khamsmya", "خمسمية", "", "zahlen"),
    ("1000", "alf", "ألف", "1000 Rial = 50 DH", "zahlen"),
    ("2000", "alfayn", "ألفين", "2000 Rial = 100 DH", "zahlen"),
    ("Wie rechnet man Rial in Dirham um?", "1 Dirham = 20 Rial", "درهم = عشرين ريال", "Rial ÷ 20 = Dirham (alf ryal = 50 DH)", "zahlen"),

    # 4. Geld & Einkaufen
    ("Geld", "flus", "فلوس", "", "geld"),
    ("Dirham / Dirhams", "derhem / drahem", "درهم / دراهم", "drahem nach 2–10: jouj drahem", "geld"),
    ("Rial", "ryal", "ريال", "1 DH = 20 Rial", "geld"),
    ("Kleingeld / Wechselgeld", "ṣarf", "صرف", "Münzen und kleine Scheine", "geld"),
    ("Hast du Kleingeld, bitte?", "ʿndek ṣ-ṣarf ʿafak?", "عندك الصرف عافاك؟", "", "geld"),
    ("Ich habe kein Kleingeld", "Ma ʿndisch ṣarf", "ما عنديش صرف", "Hört man oft von Händlern und Fahrern", "geld"),
    ("Gib mir …", "ʿṬini …", "عطيني …", "", "geld"),
    ("Gib mir bitte das Wechselgeld", "ʿAfak ʿṭini ṣ-ṣarf", "عافاك عطيني الصرف", "", "geld"),
    ("Gibt es …? / Hast du …?", "Wasch kayn …? / Wasch ʿndek …?", "واش كاين …؟ / واش عندك …؟", "", "geld"),
    ("Ein Kilo abwiegen, bitte", "ʿBer liya kilo ʿafak", "عبر ليا كيلو عافاك", "Auf dem Obst- und Gemüsemarkt", "geld"),
    ("Die Rechnung, bitte", "L-ḥsab ʿafak", "الحساب عافاك", "Im Café oder Restaurant", "geld"),
    ("groß / klein", "kbir / ṣghir", "كبير / صغير", "", "geld"),

    # 5. Taxi & Richtungen
    ("Taxi", "ṭaksi", "طاكسي", "petit taxi (Stadt) / grand taxi (Überland)", "taxi"),
    ("Taxameter / Zähler", "l-kontor", "الكونتور", "Von franz. compteur", "taxi"),
    ("Mach bitte den Zähler an", "Dir l-kontor ʿafak", "دير الكونتور عافاك", "", "taxi"),
    ("Kannst du den Zähler anmachen?", "Momkin tschʿel l-kontor ʿafak?", "ممكن تشعل الكونتور عافاك؟", "Etwas höflicher", "taxi"),
    ("Ich möchte nach … fahren", "Bghit nemschi l …", "بغيت نمشي ل …", "Bghit nemschi l-mdina = zur Altstadt", "taxi"),
    ("Wie viel bis …?", "Bschḥal l …?", "بشحال ل …؟", "Grand Taxi: vor dem Einsteigen fragen", "taxi"),
    ("Halt hier, bitte", "Wqef hna ʿafak", "وقف هنا عافاك", "", "taxi"),
    ("Wo ist …?", "Fin kayn …?", "فين كاين …؟", "Fin kayn s-suq? = Wo ist der Markt?", "taxi"),
    ("rechts", "limen", "ليمن", "", "taxi"),
    ("links", "lisser", "ليسر", "", "taxi"),
    ("geradeaus", "nischan", "نيشان", "Sir nischan = Geh geradeaus", "taxi"),
    ("Biege rechts / links ab", "Dur ʿla limen / lisser", "دور على ليمن / ليسر", "", "taxi"),
    ("hier / dort", "hna / temma", "هنا / تما", "", "taxi"),
    ("weit / nah", "bʿid / qrib", "بعيد / قريب", "Wasch bʿid wla qrib? = Weit oder nah?", "taxi"),
    ("Altstadt", "l-mdina", "المدينة", "", "taxi"),
    ("Woher kommst du?", "Mnin nta / nti?", "منين نتا / نتي؟", "nta = du (m.), nti = du (f.)", "taxi"),
]

CSS = """
.card { font-family: Arial, sans-serif; font-size: 24px; text-align: center;
        color: #222; background: #fdfaf4; }
.nightMode .card, .card.nightMode { color: #eee; background: #222; }
.darija { font-size: 30px; font-weight: bold; color: #b5462a; }
.nightMode .darija { color: #f08a65; }
.arabic { font-size: 34px; direction: rtl; margin-top: 8px;
          font-family: 'Noto Naskh Arabic', 'Geeza Pro', 'Arial', sans-serif; }
.hint { font-size: 16px; font-style: italic; color: #777; margin-top: 12px; }
"""

BACK_DARIJA = (
    "<div class='darija'>{{Darija}}</div>"
    "<div class='arabic'>{{Arabisch}}</div>"
    "{{#Hinweis}}<div class='hint'>{{Hinweis}}</div>{{/Hinweis}}"
)

MODEL = genanki.Model(
    1607392321,
    "Darija (DE ↔ Darija)",
    fields=[{"name": "Deutsch"}, {"name": "Darija"}, {"name": "Arabisch"}, {"name": "Hinweis"}],
    templates=[
        {
            "name": "Deutsch → Darija",
            "qfmt": "{{Deutsch}}",
            "afmt": "{{FrontSide}}<hr id='answer'>" + BACK_DARIJA,
        },
        {
            "name": "Darija → Deutsch",
            "qfmt": "<div class='darija'>{{Darija}}</div><div class='arabic'>{{Arabisch}}</div>",
            "afmt": "{{FrontSide}}<hr id='answer'>{{Deutsch}}"
                    "{{#Hinweis}}<div class='hint'>{{Hinweis}}</div>{{/Hinweis}}",
        },
    ],
    css=CSS,
)


class StableNote(genanki.Note):
    @property
    def guid(self):
        return genanki.guid_for(self.fields[0], self.fields[1])


def main():
    deck = genanki.Deck(2059400121, "Darija – Feilschen & Alltag")
    lines = [
        "#separator:tab",
        "#html:true",
        "#columns:Deutsch\tDarija\tArabisch\tHinweis\tTags",
        "#tags column:5",
        "#deck:Darija – Feilschen & Alltag",
    ]
    for de, darija, ar, hint, tag in VOCAB:
        deck.add_note(StableNote(model=MODEL, fields=[de, darija, ar, hint], tags=[tag]))
        lines.append("\t".join([de, darija, ar, hint, tag]))

    genanki.Package(deck).write_to_file("darija_feilschen.apkg")
    with open("darija_feilschen.txt", "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")
    print(f"{len(VOCAB)} Notizen ({2 * len(VOCAB)} Karten) geschrieben.")


if __name__ == "__main__":
    main()
