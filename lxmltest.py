from lxml import etree

nsmap = {"tei": "http://www.tei-c.org/ns/1.0"}

with open("1-100/CAT_000001.xml", mode="r") as f:
    tree = etree.parse(f)
    root = tree.getroot()
    strg = etree.tostring(tree)
    tgt = root.xpath(".//tei:desc/text()", namespaces=nsmap)
    print(tgt)
