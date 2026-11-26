def get_front_matter_html(target, kl_logo_b64):
    if target == "team":
        students_cover = """
        <div style="font-size: 11.5pt; font-weight: bold; margin-bottom: 10pt;">MUPPAVARAPU SIVARAM &nbsp;|&nbsp; 2300030447</div>
        <div style="font-size: 11.5pt; font-weight: bold;">MEDA LOHITH PAVAN KUMAR &nbsp;|&nbsp; 2300030921</div>
        """
        students_inner = """
        <div style="font-size: 11pt; font-weight: bold; margin-bottom: 8pt;">Muppavarapu Sivaram (2300030447)</div>
        <div style="font-size: 11pt; font-weight: bold;">Meda Lohith Pavan Kumar (2300030921)</div>
        """
        students_decl = """
        <div style="margin-top: 50pt;">
            <div style="font-size: 11pt; font-weight: bold; margin-bottom: 8pt;">Muppavarapu Sivaram (2300030447):</div>
            <div style="font-size: 10.5pt; margin-bottom: 45pt;">Signature ____________________ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Date: __________</div>
            <div style="font-size: 11pt; font-weight: bold; margin-bottom: 8pt;">Meda Lohith Pavan Kumar (2300030921):</div>
            <div style="font-size: 10.5pt;">Signature ____________________ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Date: __________</div>
        </div>
        """
        students_cert = """
        <div style="font-size: 11pt; font-weight: bold; line-height: 2.0; margin-top: 36pt; margin-bottom: 45pt;">
            Muppavarapu Sivaram (2300030447)<br>
            Meda Lohith Pavan Kumar (2300030921)
        </div>
        """
        margin_under_students_cover = "58pt"
        cert_ext_padding = "105pt"
    elif target == "sivaram":
        students_cover = """
        <div style="font-size: 11.5pt; font-weight: bold;">MUPPAVARAPU SIVARAM &nbsp;|&nbsp; 2300030447</div>
        """
        students_inner = """
        <div style="font-size: 11pt; font-weight: bold;">Muppavarapu Sivaram (2300030447)</div>
        """
        students_decl = """
        <div style="margin-top: 75pt;">
            <div style="font-size: 11pt; font-weight: bold; margin-bottom: 12pt;">Muppavarapu Sivaram (2300030447):</div>
            <div style="font-size: 10.5pt;">Signature ____________________ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Date: __________</div>
        </div>
        """
        students_cert = """
        <div style="font-size: 11pt; font-weight: bold; line-height: 1.8; margin-top: 40pt; margin-bottom: 50pt;">
            Muppavarapu Sivaram (2300030447)
        </div>
        """
        margin_under_students_cover = "75pt"
        cert_ext_padding = "120pt"
    else:
        students_cover = """
        <div style="font-size: 11.5pt; font-weight: bold;">MEDA LOHITH PAVAN KUMAR &nbsp;|&nbsp; 2300030921</div>
        """
        students_inner = """
        <div style="font-size: 11pt; font-weight: bold;">Meda Lohith Pavan Kumar (2300030921)</div>
        """
        students_decl = """
        <div style="margin-top: 75pt;">
            <div style="font-size: 11pt; font-weight: bold; margin-bottom: 12pt;">Meda Lohith Pavan Kumar (2300030921):</div>
            <div style="font-size: 10.5pt;">Signature ____________________ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Date: __________</div>
        </div>
        """
        students_cert = """
        <div style="font-size: 11pt; font-weight: bold; line-height: 1.8; margin-top: 40pt; margin-bottom: 50pt;">
            Meda Lohith Pavan Kumar (2300030921)
        </div>
        """
        margin_under_students_cover = "75pt"
        cert_ext_padding = "120pt"

    return f"""
<!-- ================= PAGE 1: OUTER COVER PAGE ================= -->
<div class="front-page" style="text-align: center; padding-top: 10pt;">
    <div style="margin-bottom: 14pt;">
        <img src="{kl_logo_b64}" style="width: 176pt; height: 75pt; object-fit: contain;" alt="KL University Logo">
    </div>

    <div style="font-size: 13.5pt; font-weight: bold; color: #000000; text-transform: uppercase; margin-bottom: 4pt;">
        KONERU LAKSHMAIAH EDUCATION FOUNDATION
    </div>
    <div style="font-size: 11.5pt; font-weight: bold; color: #111111; text-transform: uppercase; margin-bottom: 4pt;">
        (DEEMED TO BE UNIVERSITY)
    </div>
    <div style="font-size: 10.5pt; font-weight: bold; color: #1a1a1a; text-transform: uppercase; margin-bottom: 28pt;">
        DEPARTMENT OF EXPERIENTIAL LEARNING AND GLOBAL ENGAGEMENT
    </div>

    <div style="font-size: 14pt; font-weight: bold; text-transform: uppercase; letter-spacing: 0.5px; margin-bottom: 30pt; color: #000000;">
        FINAL PROJECT REPORT
    </div>

    <div style="font-size: 14pt; font-weight: bold; color: #183b68; line-height: 1.4; padding: 0 12pt; margin-bottom: 46pt; text-transform: uppercase;">
        SWECHA VEDIKA: A BANDWIDTH-FRUGAL, MULTILINGUAL LIVE STAGE AND KNOWLEDGE PLATFORM
    </div>

    <div style="font-size: 11.5pt; margin-bottom: 12pt;">Submitted by</div>
    <div style="margin-bottom: {margin_under_students_cover};">
        {students_cover}
    </div>

    <div style="font-size: 11.5pt; font-weight: bold; margin-bottom: 8pt;">Under the Guidance of</div>
    <div style="font-size: 13pt; font-weight: bold; margin-bottom: 2pt;">Dr. Koganti Sripath Roy</div>
    <div style="font-size: 11pt; color: #222222; margin-bottom: 2pt;">Assistant Professor</div>
    <div style="font-size: 11pt; color: #222222; margin-bottom: 105pt;">Department of EL&GE</div>

    <div style="font-size: 11.5pt; font-weight: bold; margin-bottom: 4pt;">Academic Year 2026–2027</div>
    <div style="font-size: 11pt; color: #333333; margin-bottom: 22pt;">November, 2026</div>

    <!-- Bottom metadata exactly matching reference format -->
    <div style="font-size: 9.5pt; text-align: center; line-height: 1.45; color: #111111;">
        <div><strong>Project:</strong> Swecha Vedika &nbsp;|&nbsp; <strong>Team:</strong> KL - GLUG</div>
        <div><strong>Domain:</strong> Blockchain & Cyber Security Systems</div>
    </div>
</div>


<!-- ================= PAGE 2: INNER TITLE PAGE ================= -->
<div class="front-page" style="text-align: center; padding-top: 15pt;">
    <div style="margin-bottom: 14pt;">
        <img src="{kl_logo_b64}" style="width: 155pt; height: 65pt; object-fit: contain;" alt="KL University Logo">
    </div>

    <div style="font-size: 12.5pt; font-weight: bold; color: #000000; text-transform: uppercase; margin-bottom: 3pt;">
        KONERU LAKSHMAIAH EDUCATION FOUNDATION
    </div>
    <div style="font-size: 11pt; font-weight: bold; color: #111111; text-transform: uppercase; margin-bottom: 3pt;">
        (DEEMED TO BE UNIVERSITY)
    </div>
    <div style="font-size: 10pt; font-weight: bold; color: #1a1a1a; text-transform: uppercase; margin-bottom: 24pt;">
        DEPARTMENT OF EXPERIENTIAL LEARNING AND GLOBAL ENGAGEMENT
    </div>

    <div style="font-size: 13pt; font-weight: bold; color: #183b68; line-height: 1.35; padding: 0 10pt; margin-bottom: 26pt; text-transform: uppercase;">
        SWECHA VEDIKA: A BANDWIDTH-FRUGAL, MULTILINGUAL LIVE STAGE AND KNOWLEDGE PLATFORM
    </div>

    <div style="font-size: 11pt; font-style: italic; line-height: 1.5; margin-bottom: 22pt;">
        A Capstone Project Report submitted in partial fulfilment<br>
        of the requirements for the award of the degree of
    </div>

    <div style="font-size: 13.5pt; font-weight: bold; text-transform: uppercase; margin-bottom: 4pt;">
        BACHELOR OF TECHNOLOGY
    </div>
    <div style="font-size: 11pt; font-weight: bold; margin-bottom: 30pt;">
        in Computer Science and Engineering
    </div>

    <div style="font-size: 11pt; margin-bottom: 10pt;">Submitted by</div>
    <div style="margin-bottom: 36pt;">
        {students_inner}
    </div>

    <div style="font-size: 11pt; margin-bottom: 6pt;">Faculty Guide:</div>
    <div style="font-size: 12pt; font-weight: bold; margin-bottom: 2pt;">Dr. Koganti Sripath Roy</div>
    <div style="font-size: 11pt; color: #222222; margin-bottom: 2pt;">Assistant Professor</div>
    <div style="font-size: 11pt; color: #222222; margin-bottom: 42pt;">Department of EL&GE</div>

    <div style="font-size: 11.5pt; font-weight: bold; margin-bottom: 4pt;">Academic Year 2026–2027</div>
    <div style="font-size: 10.5pt; color: #333333;">November, 2026</div>
</div>


<!-- ================= PAGE 3: STUDENT DECLARATION ================= -->
<div class="front-page">
    <div style="text-align: center; margin-top: 15px; margin-bottom: 24px;">
        <h1 style="font-size: 13pt; font-weight: bold; text-transform: uppercase; margin: 0; line-height: 1.4;">
            STUDENT DECLARATION AND ORIGINALITY STATEMENT
        </h1>
    </div>

    <p style="text-indent: 28px; line-height: 1.6; margin-bottom: 18px;">
        We declare that this capstone report titled <strong>"SWECHA VEDIKA: A BANDWIDTH-FRUGAL, MULTILINGUAL LIVE STAGE AND KNOWLEDGE PLATFORM"</strong> is an authentic record of the independent project work carried out by the undersigned team (Team: <strong>KL - GLUG</strong>) under the guidance of <strong>Dr. Koganti Sripath Roy</strong>, Assistant Professor, Department of Experiential Learning and Global Engagement (EL&GE), Koneru Lakshmaiah Education Foundation (Deemed to be University). We confirm that the implementation details, results, and claims included in the final submitted version have been checked against the team's source code, experiment records, and research diary. All external ideas and materials have been acknowledged through appropriate IEEE citations. Any AI-assisted contribution has been disclosed in the responsible-use statement.
    </p>

    <p style="text-indent: 28px; line-height: 1.6; margin-bottom: 20px;">
        We understand that the declaration must be signed by all team members and that the university may require an originality/plagiarism report.
    </p>

    {students_decl}
</div>


<!-- ================= PAGE 4: CERTIFICATE ================= -->
<div class="front-page">
    <div style="text-align: center; margin-top: 15px; margin-bottom: 24px;">
        <h1 style="font-size: 13.5pt; font-weight: bold; text-transform: uppercase; margin: 0;">
            CERTIFICATE
        </h1>
    </div>

    <p style="text-indent: 28px; line-height: 1.6; margin-bottom: 16px;">
        This is to certify that the capstone project report entitled <strong>"SWECHA VEDIKA: A BANDWIDTH-FRUGAL, MULTILINGUAL LIVE STAGE AND KNOWLEDGE PLATFORM"</strong> is submitted by the student(s) listed below, in partial fulfilment of the requirements for the academic project work under the Department of Experiential Learning and Global Engagement, Koneru Lakshmaiah Education Foundation (Deemed to be University), during the Academic Year 2026–2027.
    </p>

    <p style="text-indent: 28px; line-height: 1.6; margin-bottom: 16px;">
        The project work was carried out under the guidance of <strong>Dr. Koganti Sripath Roy</strong>, Assistant Professor, Department of Experiential Learning and Global Engagement. The final certification is subject to verification of the submitted implementation, research diary, review-gate records and evidence package.
    </p>

    {students_cert}

    <table style="width: 100%; border-collapse: collapse; margin-top: 10pt;">
        <tr>
            <td style="width: 55%; vertical-align: top;">
                <div style="font-size: 11pt; margin-bottom: 10pt;">Faculty Guide: ____________________</div>
                <div style="font-size: 10.5pt; margin-bottom: 12pt;">Date: __________</div>
                <div style="font-weight: bold; font-size: 11pt;">Dr. Koganti Sripath Roy</div>
                <div style="font-size: 9.5pt; color: #222;">Assistant Professor, Department of EL&GE</div>
            </td>
            <td style="width: 45%; vertical-align: top;">
                <div style="font-size: 11pt; margin-bottom: 10pt;">Head of Department: ________________</div>
                <div style="font-size: 10.5pt; margin-bottom: 12pt;">Date: __________</div>
                <div style="font-weight: bold; font-size: 11pt;">Dr. S. V. Aswin Kumer</div>
                <div style="font-size: 9.5pt; color: #222;">HoD, Department of EL&GE</div>
            </td>
        </tr>
        <tr>
            <td colspan="2" style="padding-top: {cert_ext_padding}; vertical-align: top;">
                <div style="font-size: 11pt; margin-bottom: 10pt;">External Examiner: ____________________</div>
                <div style="font-size: 10.5pt;">Date: __________</div>
            </td>
        </tr>
    </table>
</div>


<!-- ================= PAGE 5: ACKNOWLEDGEMENTS ================= -->
<div class="front-page">
    <div style="text-align: center; margin-top: 25px; margin-bottom: 30px;">
        <h1 style="font-size: 13.5pt; font-weight: bold; text-transform: uppercase; margin: 0;">
            ACKNOWLEDGEMENTS
        </h1>
    </div>

    <p style="text-indent: 28px; line-height: 1.68; margin-bottom: 22px; font-size: 11pt;">
        The team expresses its sincere gratitude to the faculty guide, <strong>Dr. Koganti Sripath Roy</strong>, Assistant Professor, Department of Experiential Learning and Global Engagement, for his valuable guidance, continuous support, and academic encouragement throughout the development of the project titled <strong>"SWECHA VEDIKA: A BANDWIDTH-FRUGAL, MULTILINGUAL LIVE STAGE AND KNOWLEDGE PLATFORM."</strong>
    </p>

    <p style="text-indent: 28px; line-height: 1.68; margin-bottom: 22px; font-size: 11pt;">
        The team would like to express its heartfelt gratitude to <strong>Dr. T. K. Rama Krishna Rao</strong>, Principal, College of Engineering; <strong>Dr. S. V. Aswin Kumer</strong>, HoD, EL&GE; and <strong>Dr. P. Gopi Krishna</strong>, Alternate HoD, for their valuable support, encouragement, and administrative guidance throughout the project.
    </p>

    <p style="text-indent: 28px; line-height: 1.68; font-size: 11pt;">
        The team also sincerely acknowledges the Department of Experiential Learning and Global Engagement and Koneru Lakshmaiah Education Foundation (Deemed to be University) for providing the academic environment in which the capstone work was undertaken. The team thanks all faculty members and individuals who provided feedback during project reviews and evaluation.
    </p>
</div>
"""
