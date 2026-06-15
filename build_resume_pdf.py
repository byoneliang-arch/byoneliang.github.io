from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.cidfonts import UnicodeCIDFont
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    ListFlowable,
    ListItem,
    HRFlowable,
)


OUT_PDF = "梁博一-实习简历.pdf"

pdfmetrics.registerFont(UnicodeCIDFont("STSong-Light"))


def link(label, url):
    return f'<a href="{url}" color="#1f5fa8"><u>{label}</u></a>'


def p(text, style):
    return Paragraph(text, style)


def bullets(items, style):
    return ListFlowable(
        [ListItem(Paragraph(item, style), leftIndent=10) for item in items],
        bulletType="bullet",
        start="circle",
        leftIndent=14,
        bulletFontName="STSong-Light",
        bulletFontSize=8,
        bulletOffsetY=1,
    )


def section(title, styles):
    return [
        Spacer(1, 7),
        Paragraph(title, styles["section"]),
        HRFlowable(width="100%", thickness=0.7, color=colors.HexColor("#d9e2f3"), spaceBefore=2, spaceAfter=5),
    ]


def project(name, links, tech, desc, items, styles):
    story = [
        Paragraph(name, styles["project_title"]),
        Paragraph("链接：" + "  |  ".join(link(label, url) for label, url in links), styles["meta"]),
        Paragraph(f"<b>技术栈：</b>{tech}", styles["meta"]),
        Paragraph(desc, styles["body"]),
        bullets(items, styles["bullet"]),
    ]
    return story


def build():
    doc = SimpleDocTemplate(
        OUT_PDF,
        pagesize=letter,
        leftMargin=0.7 * inch,
        rightMargin=0.7 * inch,
        topMargin=0.55 * inch,
        bottomMargin=0.55 * inch,
        title="梁博一-实习简历",
        author="梁博一",
    )

    styles = getSampleStyleSheet()
    styles.add(ParagraphStyle(
        name="name",
        fontName="STSong-Light",
        fontSize=20,
        leading=24,
        alignment=TA_CENTER,
        textColor=colors.HexColor("#0b2545"),
        spaceAfter=3,
    ))
    styles.add(ParagraphStyle(
        name="target",
        fontName="STSong-Light",
        fontSize=10.5,
        leading=14,
        alignment=TA_CENTER,
        textColor=colors.HexColor("#1f4d78"),
        spaceAfter=5,
    ))
    styles.add(ParagraphStyle(
        name="contact",
        fontName="STSong-Light",
        fontSize=9.3,
        leading=12,
        alignment=TA_CENTER,
        textColor=colors.HexColor("#555555"),
        spaceAfter=8,
    ))
    styles.add(ParagraphStyle(
        name="section",
        fontName="STSong-Light",
        fontSize=12.2,
        leading=15,
        textColor=colors.HexColor("#2e74b5"),
        spaceBefore=2,
        spaceAfter=0,
    ))
    styles.add(ParagraphStyle(
        name="body",
        fontName="STSong-Light",
        fontSize=9.3,
        leading=13,
        alignment=TA_LEFT,
        textColor=colors.HexColor("#202020"),
        spaceAfter=4,
    ))
    styles.add(ParagraphStyle(
        name="bullet",
        fontName="STSong-Light",
        fontSize=9.1,
        leading=12.2,
        textColor=colors.HexColor("#202020"),
        spaceAfter=1.4,
    ))
    styles.add(ParagraphStyle(
        name="meta",
        fontName="STSong-Light",
        fontSize=8.8,
        leading=11.5,
        textColor=colors.HexColor("#555555"),
        spaceAfter=2,
    ))
    styles.add(ParagraphStyle(
        name="project_title",
        fontName="STSong-Light",
        fontSize=10.7,
        leading=13.5,
        textColor=colors.HexColor("#1f4d78"),
        spaceBefore=4,
        spaceAfter=2,
    ))

    story = [
        Paragraph("梁博一", styles["name"]),
        Paragraph("求职意向：AI 应用开发实习", styles["target"]),
        Paragraph(
            '深圳  |  18859047927  |  '
            + link("byoneliang@gmail.com", "mailto:byoneliang@gmail.com")
            + "  |  "
            + link("GitHub", "https://github.com/byoneliang-arch")
            + "  |  "
            + link("个人主页", "https://byoneliang-arch.github.io/byoneliang.github.io/"),
            styles["contact"],
        ),
    ]

    story += section("个人简介", styles)
    story.append(Paragraph(
        "深圳北理莫斯科大学数学与物理专业本科生，2024 级大二，预计 2028 年毕业。"
        "正在系统学习 Python 编程、AI 应用开发、RAG、Agent 开发与 GitHub 项目开发。"
        "已独立完成并部署 AI PDF 工具、Canvas 横版小游戏和数据可视化全栈应用，"
        "希望在实习中继续提升工程能力、AI 应用开发能力和产品落地能力。",
        styles["body"],
    ))

    story += section("教育经历", styles)
    story.append(Paragraph("<b>深圳北理莫斯科大学</b>  |  数学与物理专业 本科  |  2024 级 大二，预计 2028 年毕业", styles["body"]))
    story.append(bullets([
        "相关基础：数学分析、高等代数、概率统计、物理建模、编程基础等。",
        "重点方向：AI 应用开发、Python 编程、数据分析、Web 项目开发。",
    ], styles["bullet"]))

    story += section("技能", styles)
    story.append(bullets([
        "编程语言：Python、JavaScript、HTML、CSS",
        "AI 应用：AI 应用开发、RAG 基础、Agent 开发基础、Streamlit",
        "Web 开发：Vue 3、Vite、Flask、Canvas、响应式页面开发",
        "数据与可视化：ECharts、SQLite、CSV/Excel 数据处理、基础数据分析",
        "工程工具：Git、GitHub、Docker、Gunicorn、Render、GitHub Actions",
        "其他：机器学习基础、数学与物理建模思维",
    ], styles["bullet"]))

    story += section("项目经历", styles)
    story += project(
        "AI PDF 知识助手",
        [("GitHub", "https://github.com/byoneliang-arch/ai-pdf-assistant"), ("在线演示", "https://ai-pdf-assistant-lby.streamlit.app/")],
        "Python、Streamlit",
        "支持上传 PDF 并进行智能检索的 AI 工具，面向文档阅读、资料查询和知识问答场景。",
        [
            "使用 Streamlit 搭建 Web 交互界面，实现 PDF 上传与检索结果展示。",
            "围绕 PDF 文档信息检索流程进行功能设计，提升用户查询资料的效率。",
            "将项目部署到线上演示环境，并通过 GitHub 管理项目代码。",
            "熟悉了 Python Web 小工具从功能设计、代码实现到线上部署的完整流程。",
        ],
        styles,
    )

    story += project(
        "小猪大冒险",
        [("GitHub", "https://github.com/byoneliang-arch/pig-adventure1"), ("在线演示", "https://byoneliang-arch.github.io/pig-adventure1/")],
        "HTML、CSS、JavaScript、Canvas",
        "原创像素风 2D 横版网页小游戏，包含森林、暮色山地、雪山冰湖三关，以及金币收集、障碍规避、踩怪和终点判定。",
        [
            "使用 Canvas 实现 2D 游戏画面绘制、角色移动、关卡场景和基础碰撞逻辑。",
            "使用原生 HTML、CSS、JavaScript 完成游戏页面与交互逻辑，部署到 GitHub Pages。",
            "通过完整小游戏项目训练了交互设计、动画循环、状态管理和前端调试能力。",
        ],
        styles,
    )

    story += project(
        "本地数据记录与多折线图分析工具",
        [("GitHub", "https://github.com/byoneliang-arch/line-chart-tool"), ("在线演示", "https://line-chart-tool.onrender.com")],
        "Vue 3、Vite、ECharts、Flask、SQLite、Docker、Gunicorn、Render、GitHub Actions",
        "用于记录和分析日期型数据的全栈 Web 应用，支持多条自定义折线、日期筛选、数据编辑、最大最小值标记、CSV/Excel 导出和图表导出。",
        [
            "使用 Vue 3 和 Vite 构建前端界面，实现数据录入、编辑、筛选和交互式图表展示。",
            "使用 ECharts 实现多折线趋势分析、最大值/最小值标记和图表导出能力。",
            "使用 Flask 与 SQLite 搭建后端接口和数据存储逻辑，并通过 Docker、Gunicorn、Render 完成部署。",
            "完整实践了前后端分离项目的开发、部署和维护流程。",
        ],
        styles,
    )

    story += section("自我评价", styles)
    story.append(bullets([
        "具备数学与物理背景，逻辑分析能力较强，适合处理 AI 应用、数据分析和工程问题。",
        "有持续完成实际项目的习惯，能够从需求出发独立完成开发、部署和迭代。",
        "对 AI 应用开发、AI 游戏开发、RAG 系统和 Agent 开发保持长期学习兴趣，希望在真实业务中继续提升工程能力。",
        "目前仍在持续开发 AI 项目、游戏项目和个人作品集项目，不断通过实际项目提升工程实践能力。",
    ], styles["bullet"]))

    def white_background(canvas, doc_obj):
        canvas.saveState()
        canvas.setFillColor(colors.white)
        canvas.rect(0, 0, doc_obj.pagesize[0], doc_obj.pagesize[1], fill=1, stroke=0)
        canvas.restoreState()

    doc.build(story, onFirstPage=white_background, onLaterPages=white_background)


if __name__ == "__main__":
    build()
