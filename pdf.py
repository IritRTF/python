from fpdf import FPDF, HTMLMixin
from prettytable import PrettyTable
class PDF(FPDF, HTMLMixin):
    pass
pdf = PDF()
pdf.add_page()
pdf.add_font("Sans", style="", fname="Noto_Sans/NotoSans-Regular.ttf", uni=True)
# подключаем жирный шрифт "Sans"
pdf.add_font("Sans", style="B", fname="Noto_Sans/NotoSans-Bold.ttf", uni=True)
# подключаем наклонный шрифт "Sans"
pdf.add_font("Sans", style="I", fname="Noto_Sans/NotoSans-Italic.ttf", uni=True)
# подключаем жирный-наклонный шрифт "Sans"
pdf.add_font("Sans", style="BI", fname="Noto_Sans/NotoSans-BoldItalic.ttf", uni=True)
# установить подключенный шрифт "Sans" по умолчанию для всего документа
pdf.set_font("Sans")
pdf.set_font_size(6)

years_salary_dic = {2007: 38916, 2008: 43646, 2009: 42492, 2010: 43846, 2011: 47451, 2012: 48243, 2013: 51510,
                            2014: 50658, 2015: 52696, 2016: 62675, 2017: 60935, 2018: 58335, 2019: 69467, 2020: 73431,
                            2021: 82690, 2022: 91795}
years_count_dic = {2007: 2196, 2008: 17549, 2009: 17709, 2010: 29093, 2011: 36700, 2012: 44153, 2013: 59954,
                           2014: 66837, 2015: 70039, 2016: 75145, 2017: 82823, 2018: 131701, 2019: 115086, 2020: 102243,
                           2021: 57623, 2022: 18294}
years_salary_vac_dic = {2007: 43770, 2008: 50412, 2009: 46699, 2010: 50570, 2011: 55770, 2012: 57960,
                                2013: 58804, 2014: 62384, 2015: 62322, 2016: 66817, 2017: 72460, 2018: 76879,
                                2019: 85300, 2020: 89791, 2021: 100987, 2022: 116651}
years_count_vac_dic = {2007: 317, 2008: 2460, 2009: 2066, 2010: 3614, 2011: 4422, 2012: 4966, 2013: 5990,
                               2014: 5492, 2015: 5375, 2016: 7219, 2017: 8105, 2018: 10062, 2019: 9016, 2020: 7113,
                               2021: 3466, 2022: 1115}
area_salary_dic = {'Москва': 76970, 'Санкт-Петербург': 65286, 'Новосибирск': 62254, 'Екатеринбург': 60962,
                           'Казань': 52580, 'Краснодар': 51644, 'Челябинск': 51265, 'Самара': 50994, 'Пермь': 48089,
                           'Нижний Новгород': 47662}
area_count_dic = {'Москва': 0.3246, 'Санкт-Петербург': 0.1197, 'Новосибирск': 0.0271, 'Казань': 0.0237,
                          'Нижний Новгород': 0.0232, 'Ростов-на-Дону': 0.0209, 'Екатеринбург': 0.0207,
                          'Краснодар': 0.0185, 'Самара': 0.0143, 'Воронеж': 0.0141}


pdf.cell(38, 5, "Два Года", border=1)
pdf.cell(38, 5, "Ср.З/П", border=1)
pdf.cell(38, 5, "Ср.З/П - Программист", border=1)
pdf.cell(38, 5, "Кол-во вакансий", border=1)
pdf.cell(38, 5, "Кол-во вакансий - Программист", border=1, ln=0)
pdf.ln()


for row, (year, value) in enumerate(years_salary_dic.items(), start=2):
    pdf.cell(38, 5, str(year), border=1)
    pdf.cell(38, 5, str(value), border=1)
    pdf.cell(38, 5, str(years_salary_vac_dic[year]), border=1)
    pdf.cell(38, 5, str(years_count_dic[year]), border=1)
    pdf.cell(38, 5, str(years_count_vac_dic[year]), border=1)
    pdf.ln()

pdf.output("simple_demo.pdf")







