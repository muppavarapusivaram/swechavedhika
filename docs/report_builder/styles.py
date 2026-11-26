CSS_STYLES = """
@page {
    size: A4 portrait;
    margin-top: 24mm;
    margin-bottom: 22mm;
    margin-left: 30mm;
    margin-right: 22mm;
}

@page :first {
    margin-top: 15mm;
    margin-bottom: 15mm;
    margin-left: 30mm;
    margin-right: 22mm;
}

*, *::before, *::after {
    box-sizing: border-box;
}

body {
    font-family: 'Times New Roman', Times, serif;
    font-size: 11pt;
    line-height: 1.42;
    color: #000000;
    margin: 0;
    padding: 0;
    text-align: justify;
}

.page-break {
    page-break-before: always;
    break-before: page;
}

.front-page {
    page-break-after: always;
    break-after: page;
}

h1.chapter-title {
    font-size: 13.5pt;
    font-weight: bold;
    text-transform: uppercase;
    text-align: center;
    margin-top: 6pt;
    margin-bottom: 12pt;
    color: #000000;
    page-break-after: avoid;
    break-after: avoid;
}

h2.section-heading {
    font-size: 11.5pt;
    font-weight: bold;
    margin-top: 11pt;
    margin-bottom: 4pt;
    color: #000000;
    page-break-after: avoid;
    break-after: avoid;
}

h3.sub-heading {
    font-size: 10.5pt;
    font-weight: bold;
    margin-top: 8pt;
    margin-bottom: 3pt;
    color: #000000;
    page-break-after: avoid;
    break-after: avoid;
}

p {
    margin: 0 0 5pt 0;
    text-align: justify;
    text-justify: inter-word;
    orphans: 3;
    widows: 3;
}

ul, ol {
    margin: 2pt 0 5pt 16pt;
    padding: 0;
    orphans: 3;
    widows: 3;
}

li {
    margin-bottom: 2.5pt;
    text-align: justify;
}

table.report-table {
    width: 100%;
    border-collapse: collapse;
    margin: 6pt 0 8pt 0;
    font-size: 8.5pt;
    page-break-inside: auto;
}

table.report-table th {
    background-color: #f2f2f2;
    border: 1pt solid #444;
    padding: 3.5pt 5pt;
    text-align: left;
    font-weight: bold;
}

table.report-table td {
    border: 1pt solid #666;
    padding: 3pt 5pt;
    vertical-align: top;
}

tr {
    page-break-inside: avoid;
    break-inside: avoid;
}

.figures-grid {
    display: flex;
    flex-wrap: wrap;
    justify-content: space-between;
    gap: 8px;
    margin: 8pt 0;
    page-break-inside: avoid;
    break-inside: avoid;
}

.figures-grid .fig-col {
    width: 48.5%;
    text-align: center;
}

.figures-grid img {
    width: 100%;
    max-height: 115px;
    object-fit: contain;
    border: 1pt solid #bbb;
    border-radius: 2px;
}

.figure-box {
    text-align: center;
    margin: 6pt auto;
    page-break-inside: avoid;
    break-inside: avoid;
}

.figure-box img {
    max-height: 125px;
    max-width: 85%;
    border: 1pt solid #bbb;
    border-radius: 2px;
    object-fit: contain;
}

.figure-caption {
    font-size: 8pt;
    font-weight: bold;
    margin-top: 3pt;
    text-align: center;
}

.equation-box {
    margin: 6pt 0;
    padding: 3.5pt 8pt;
    background: #fdfdfd;
    border: 1pt solid #ddd;
    font-family: 'Courier New', monospace;
    font-size: 8.5pt;
    display: flex;
    justify-content: space-between;
    align-items: center;
    page-break-inside: avoid;
    break-inside: avoid;
}

.toc-table {
    width: 100%;
    border-collapse: collapse;
    margin: 2pt 0;
    font-size: 9.5pt;
}

.toc-table td {
    padding: 1.5pt 0;
    vertical-align: bottom;
}

.toc-table .toc-title {
    text-align: left;
}

.toc-table .toc-page {
    text-align: right;
    width: 32px;
    font-weight: bold;
}

.signature-table {
    width: 100%;
    margin-top: 20px;
    border-collapse: collapse;
}

.signature-table td {
    padding: 8px 4px;
    vertical-align: top;
}
"""
