Python 2.7.14 (v2.7.14:84471935ed, Sep 16 2017, 20:25:58) [MSC v.1500 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
# функция генерации
def html_gen(title, body, text_color, bg_color, bold, italic, size):
    output = "<html>"
    output += "<title>" + title + "</title>"
    output += "<body>"
    output += "<font size=" + size + ">"

    if (bold == 1):
        output += "<b>"
    if (italic == 1):
        output += "<i>"
    output += body
    if (bold == 1):
        output += "</b>"
    if (italic == 1):
        output += "</i>"

    output += "</font>"
    output += "<body text=" + text_color + ">"
    output += "<body bgcolor=" + bg_color + ">"
    output += "</body>"
    output += "</html>"

    f = open('akkulov_page.html', 'w')
    f.write(output)
    f.close()

def main():
    # RGB код интересующего Вас цвета
    # https://www.rapidtables.com/web/color/RGB_Color.html

############################################################################
#               ПАРАМЕТРЫ ГЕНЕРАЦИИ ПОЗОРНОГО HTML ДОКУМЕНТА
    page_title = "ИФНиТ" # заголовок
    page_body = "ИНСТИТУТ ФИЗИКИ, НАНОТЕХНОЛОГИЙ И ТЕЛЕКОММУНИКАЦИЙ" # текст документа
    text_color = "000000"  # цвет текста в документе
    bg_color = "BECFFF"  # цвет фона в документе
    bold_text = 1 # жирный шрифт (0-1)
    italic_text = 0 # курсивный шрифт (0-1)
    text_size = "3"  # размер текста (0-7)
############################################################################

    html_gen(page_title, page_body, text_color, bg_color, bold_text, italic_text, text_size)

main()
