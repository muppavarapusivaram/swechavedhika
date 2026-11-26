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
        <tr>
            <td style="width: 50%; font-weight: bold;">Muppavarapu Sivaram (2300030447):</td>
            <td style="width: 50%;">Signature ____________________ &nbsp; Date: __________</td>
        </tr>
        <tr>
            <td style="width: 50%; font-weight: bold;">Meda Lohith Pavan Kumar (2300030921):</td>
            <td style="width: 50%;">Signature ____________________ &nbsp; Date: __________</td>
        </tr>
        """
        students_cert = """
        <div style="font-size: 11pt; font-weight: bold; margin: 12px 0 16px 0;">
            1. Muppavarapu Sivaram (2300030447)<br>
            2. Meda Lohith Pavan Kumar (2300030921)
        </div>
        """
        margin_under_students_cover = "58pt"
    elif target == "sivaram":
        students_cover = """
        <div style="font-size: 11.5pt; font-weight: bold;">MUPPAVARAPU SIVARAM &nbsp;|&nbsp; 2300030447</div>
        """
        students_inner = """
        <div style="font-size: 11pt; font-weight: bold;">Muppavarapu Sivaram (2300030447)</div>
        """
        students_decl = """
        <tr>
            <td style="width: 50%; font-weight: bold;">Muppavarapu Sivaram (2300030447):</td>
            <td style="width: 50%;">Signature ____________________ &nbsp; Date: __________</td>
        </tr>
        """
        students_cert = """
        <div style="font-size: 11pt; font-weight: bold; margin: 12px 0 16px 0;">
            Muppavarapu Sivaram (2300030447)
        </div>
        """
        margin_under_students_cover = "75pt"
    else:
        students_cover = """
        <div style="font-size: 11.5pt; font-weight: bold;">MEDA LOHITH PAVAN KUMAR &nbsp;|&nbsp; 2300030921</div>
        """
        students_inner = """
        <div style="font-size: 11pt; font-weight: bold;">Meda Lohith Pavan Kumar (2300030921)</div>
        """
        students_decl = """
        <tr>
            <td style="width: 50%; font-weight: bold;">Meda Lohith Pavan Kumar (2300030921):</td>
            <td style="width: 50%;">Signature ____________________ &nbsp; Date: __________</td>
        </tr>
        """
        students_cert = """
        <div style="font-size: 11pt; font-weight: bold; margin: 12px 0 16px 0;">
            Meda Lohith Pavan Kumar (2300030921)
        </div>
        """
        margin_under_students_cover = "75pt"

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
        <div><strong>Project:</strong> Swecha Vedika &nbsp;|&nbsp; <strong>Team:</strong> Y23-HTE KL-KLUG</div>
        <div><strong>Domain:</strong> Blockchain & Cyber Security Systems</div>
    </div>
</div>


<!-- ================= PAGE 2: INNER TITLE PAGE ================= -->
<div class="front-page" style="text-align: center; padding-top: 15pt;">
    <div style="margin-bottom: 12pt;">
        <img src="{kl_logo_b64}" style="width: 155pt; height: 65pt; object-fit: contain;" alt="KL University Logo">
    </div>

    <div style="font-size: 12.5pt; font-weight: bold; color: #000000; text-transform: uppercase; margin-bottom: 3pt;">
        KONERU LAKSHMAIAH EDUCATION FOUNDATION
    </div>
    <div style="font-size: 11pt; font-weight: bold; color: #111111; text-transform: uppercase; margin-bottom: 3pt;">
        (DEEMED TO BE UNIVERSITY)
    </div>
    <div style="font-size: 10pt; font-weight: bold; color: #1a1a1a; text-transform: uppercase; margin-bottom: 22pt;">
        DEPARTMENT OF EXPERIENTIAL LEARNING AND GLOBAL ENGAGEMENT
    </div>

    <div style="font-size: 13pt; font-weight: bold; color: #183b68; line-height: 1.35; padding: 0 10pt; margin-bottom: 24pt; text-transform: uppercase;">
        SWECHA VEDIKA: A BANDWIDTH-FRUGAL, MULTILINGUAL LIVE STAGE AND KNOWLEDGE PLATFORM
    </div>

    <div style="font-size: 11pt; font-style: italic; line-height: 1.5; margin-bottom: 20pt;">
        A Capstone Project Report submitted in partial fulfilment<br>
        of the requirements for the award of the degree of
    </div>

    <div style="font-size: 13.5pt; font-weight: bold; text-transform: uppercase; margin-bottom: 4pt;">
        BACHELOR OF TECHNOLOGY
    </div>
    <div style="font-size: 11pt; font-weight: bold; margin-bottom: 26pt;">
        in Computer Science and Engineering
    </div>

    <div style="font-size: 11pt; margin-bottom: 8pt;">Submitted by</div>
    <div style="margin-bottom: 30pt;">
        {students_inner}
    </div>

    <div style="font-size: 11pt; margin-bottom: 4pt;">Faculty Guide:</div>
    <div style="font-size: 12pt; font-weight: bold; margin-bottom: 2pt;">Dr. Koganti Sripath Roy</div>
    <div style="font-size: 11pt; color: #222222; margin-bottom: 2pt;">Assistant Professor</div>
    <div style="font-size: 11pt; color: #222222; margin-bottom: 30pt;">Department of EL&GE</div>

    <div style="font-size: 11.5pt; font-weight: bold; margin-bottom: 3pt;">Academic Year 2026–2027</div>
    <div style="font-size: 10.5pt; color: #333333;">November, 2026</div>
</div>


<!-- ================= PAGE 3: STUDENT DECLARATION ================= -->
<div class="front-page">
    <div style="text-align: center; margin-top: 10px; margin-bottom: 18px;">
        <h1 style="font-size: 13pt; font-weight: bold; text-transform: uppercase; margin: 0; line-height: 1.4;">
            STUDENT DECLARATION AND ORIGINALITY STATEMENT
        </h1>
    </div>

    <p style="text-indent: 28px; line-height: 1.55;">
        We declare that this capstone report titled <strong>"SWECHA VEDIKA: A BANDWIDTH-FRUGAL, MULTILINGUAL LIVE STAGE AND KNOWLEDGE PLATFORM"</strong> is an authentic record of the independent project work carried out by the undersigned team (Team: <strong>Y23-HTE KL-KLUG</strong>) under the guidance of <strong>Dr. Koganti Sripath Roy</strong>, Assistant Professor, Department of Experiential Learning and Global Engagement (EL&GE), Koneru Lakshmaiah Education Foundation (Deemed to be University).
    </p>

    <p style="text-indent: 28px; line-height: 1.55;">
        We confirm that the architectural formulations, low-bandwidth WebRTC adaptation algorithms, WhatsApp finite-state conversational integration, Indic speech-to-text pipelines, implementation source code, experiment records, and evaluation benchmarks presented in this report have been verified against the project repository, local testbed logs, and actual system execution traces. All external software libraries, open-source frameworks, and academic literature referenced herein have been duly acknowledged through formal IEEE citations. Any generative artificial intelligence assistance utilized for syntactic refinement or modular scaffolding has been transparently disclosed in the Responsible AI-Tool Disclosure section.
    </p>

    <p style="text-indent: 28px; line-height: 1.55;">
        We understand that this declaration is binding upon all team members and that the university reserves the right to subject the document and accompanying artifacts to academic integrity audits and similarity screening.
    </p>

    <table class="signature-table">
        {students_decl}
    </table>
</div>


<!-- ================= PAGE 4: CERTIFICATE ================= -->
<div class="front-page">
    <div style="text-align: center; margin-top: 10px; margin-bottom: 18px;">
        <h1 style="font-size: 13pt; font-weight: bold; text-transform: uppercase; margin: 0;">
            CERTIFICATE
        </h1>
    </div>

    <p style="text-indent: 28px; line-height: 1.55;">
        This is to certify that the capstone project report entitled <strong>"SWECHA VEDIKA: A BANDWIDTH-FRUGAL, MULTILINGUAL LIVE STAGE AND KNOWLEDGE PLATFORM"</strong> is submitted by the student(s) listed below, in partial fulfilment of the requirements for the award of the degree of <strong>Bachelor of Technology in Computer Science and Engineering</strong> under the Department of Experiential Learning and Global Engagement (EL&GE), Koneru Lakshmaiah Education Foundation (Deemed to be University), during the Academic Year 2026–2027:
    </p>

    <div style="padding-left: 28px;">
        {students_cert}
    </div>

    <p style="text-indent: 28px; line-height: 1.55;">
        The project work was carried out under the guidance of <strong>Dr. Koganti Sripath Roy</strong>, Assistant Professor, Department of Experiential Learning and Global Engagement. The technical execution, system architecture, empirical test results, and final documentation have been scrutinized, validated, and found satisfactory for the external project evaluation.
    </p>

    <table style="width: 100%; margin-top: 45px; border-collapse: collapse;">
        <tr>
            <td style="width: 50%; vertical-align: top;">
                <div style="font-weight: bold;">Dr. Koganti Sripath Roy</div>
                <div style="font-size: 9.5pt;">Faculty Guide & Assistant Professor</div>
                <div style="font-size: 9.5pt;">Department of EL&GE</div>
                <div style="margin-top: 15px; font-size: 9pt;">Signature: ____________________</div>
                <div style="margin-top: 4px; font-size: 9pt;">Date: ________________________</div>
            </td>
            <td style="width: 50%; vertical-align: top; text-align: right;">
                <div style="font-weight: bold;">Dr. S. V. Aswin Kumer</div>
                <div style="font-size: 9.5pt;">Head of Department (HoD)</div>
                <div style="font-size: 9.5pt;">Department of EL&GE</div>
                <div style="margin-top: 15px; font-size: 9pt;">Signature: ____________________</div>
                <div style="margin-top: 4px; font-size: 9pt;">Date: ________________________</div>
            </td>
        </tr>
        <tr>
            <td colspan="2" style="padding-top: 35px; text-align: center;">
                <div style="font-weight: bold;">External Examiner</div>
                <div style="font-size: 9.5pt;">Signature: ____________________________________ &nbsp;&nbsp;&nbsp;&nbsp; Date: __________________</div>
            </td>
        </tr>
    </table>
</div>


<!-- ================= PAGE 5: ACKNOWLEDGEMENTS ================= -->
<div class="front-page">
    <div style="text-align: center; margin-top: 10px; margin-bottom: 18px;">
        <h1 style="font-size: 13pt; font-weight: bold; text-transform: uppercase; margin: 0;">
            ACKNOWLEDGEMENTS
        </h1>
    </div>

    <p style="text-indent: 28px; line-height: 1.55;">
        The team expresses its deepest and most sincere gratitude to our esteemed faculty guide, <strong>Dr. Koganti Sripath Roy</strong>, Assistant Professor, Department of Experiential Learning and Global Engagement (EL&GE), for his invaluable mentorship, rigorous academic critique, continuous technical guidance, and steadfast encouragement throughout the conception, architecture, implementation, and empirical validation of <strong>Swecha Vedika</strong>.
    </p>

    <p style="text-indent: 28px; line-height: 1.55;">
        We extend our heartfelt appreciation to <strong>Dr. T. K. Rama Krishna Rao</strong>, Principal, College of Engineering, KLEF; <strong>Dr. S. V. Aswin Kumer</strong>, Head of Department, EL&GE; and <strong>Dr. P. Gopi Krishna</strong>, Alternate Head of Department, EL&GE, for their visionary administrative support, provision of exceptional computational infrastructure, and constant academic facilitation during the capstone progression.
    </p>

    <p style="text-indent: 28px; line-height: 1.55;">
        We also express our sincere gratitude to the <strong>Swecha Telangana</strong> free and open-source software community for providing grassroots domain insights into the acute telecommunication constraints faced by rural students, self-help groups, and non-profit educational initiatives across rural Andhra Pradesh and Telangana.
    </p>

    <p style="text-indent: 28px; line-height: 1.55;">
        Finally, we thank our parents, peers, lab coordinators, and faculty reviewers whose insightful critiques during milestone reviews G0, R1, PDR, and CDR significantly strengthened the architectural rigor, fault resilience, and practical relevance of this capstone endeavor.
    </p>
</div>
"""
