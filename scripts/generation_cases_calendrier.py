from pathlib import Path


_HERE = Path(__file__).parent



CASE_TEMPLATE = """\
  <div class="case">
    <a href="{url}" target="_blank">
      <div class="case_text stroke-text smooth-16">
        <b>
        {number}
        </br>
        {text}
        </b>
      </div>
    </a>
  </div>
"""


def main():
    urls = [
        "https://irmo322.github.io/avent-maman-2024/jour1_dabhikpa.html",
        "https://irmo322.github.io/avent-maman-2024/jour2_ftgpwkeo.html",
        "https://irmo322.github.io/avent-maman-2024/jour3_gcjprmq.html",
        "https://irmo322.github.io/avent-maman-2024/jour4_qpamwkel.html",
        "https://irmo322.github.io/avent-maman-2024/jour5_fpartidb.html",
        "https://irmo322.github.io/avent-maman-2024/jour6_angielfh.html",
        "https://irmo322.github.io/avent-maman-2024/jour7_cvknszoh.html",
        "https://irmo322.github.io/avent-maman-2024/jour8_cnegmlsd.html",
        "https://irmo322.github.io/avent-maman-2024/jour9_fprlskog.html",
        "https://irmo322.github.io/avent-maman-2024/jour10_enchspld.html",
        "https://irmo322.github.io/avent-maman-2024/jour11_dkeospwl.html",
        "https://irmo322.github.io/avent-maman-2024/jour12_amlsiofg.html",
        "https://irmo322.github.io/avent-maman-2024/jour13_nsporjkf.html",
        "https://irmo322.github.io/avent-maman-2024/jour14_qpmlgtds.html",
        "https://irmo322.github.io/avent-maman-2024/jour15_rgbjkiqf.html",
        "https://irmo322.github.io/avent-maman-2024/jour16_olesncjr.html",
        "https://irmo322.github.io/avent-maman-2024/jour17_ecsjlopf.html",
        "https://irmo322.github.io/avent-maman-2024/jour18_zxjsmpfl.html",
        "https://irmo322.github.io/avent-maman-2024/jour19_snxmdlof.html",
        "https://irmo322.github.io/avent-maman-2024/jour20_zecqkodg.html",
        "https://irmo322.github.io/avent-maman-2024/jour21_xcmlpfgt.html",
        "https://irmo322.github.io/avent-maman-2024/jour22_scnjdmpl.html",
        "https://irmo322.github.io/avent-maman-2024/jour23_snxqplme.html",
        "https://irmo322.github.io/avent-maman-2024/jour24_sglpmftl.html",
    ]
    
    texts = [
        "Coulisses",
        "Mère Cloclo 1",
        "Méditation",
        "Odyssée 1",
        "Mère Cloclo 2",
        "Beau gosse allemand",
        "Maman qui danse",
        "Odyssée 2",
        "Choré de Nöel",
        "Rétrospective",
        "Mère Cloclo 3",
        "Lutin en retard",
        "Choré Charlie",
        "Mère Cloclo 4",
        "Encore en retard",
        "Rumi",
        "Choré Alice",
        "Mère Cloclo 5",
        "Odyssée 3",
        "Murmuration",
        "Mère Cloclo 6",
        "Odyssée 3.5 ?",
        "Live at Crozon",
        "Les poussins",
    ]
    
    assert len(urls) == len(texts)
    
    with open("cases.html", "w", encoding='utf-8') as f:
        for i, (url, text) in enumerate(zip(urls, texts)):
            case_html_text = CASE_TEMPLATE.format(url=url, number=i+1, text=text)
            f.write(case_html_text)


if __name__ == "__main__":
    main()

