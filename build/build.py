"""공통 엔진 + 보일 권들의 내용 + three.js를 합쳐 HTML 파일 하나를 만든다.

사용: python3 -I build.py
보일 권은 아래 VISIBLE에서 고른다. 고른 순서대로 왼쪽 책장에 꽂힌다.
"""
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUT = HERE.parent / "웨이팅룸_코드_읽기.html"
TITLE = "웨이팅룸 코드 읽기"

VISIBLE = [1, 2, 3, 4, 5]


def main():
    engine = (HERE / "engine.html").read_text(encoding="utf-8")
    three = (HERE / "vendor" / "three.min.js").read_text(encoding="utf-8").replace("</script", "<\\/script")
    volumes = "\n".join((HERE / f"vol{n}.js").read_text(encoding="utf-8") for n in VISIBLE)
    html = (engine
            .replace("/*TITLE*/", TITLE)
            .replace("/*VOLUMES*/", volumes)
            .replace("/*THREE*/", three))
    OUT.write_text(html, encoding="utf-8")
    print(f"{OUT} · {VISIBLE}권 · {len(html) // 1024}KB")


main()
