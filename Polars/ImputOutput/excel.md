1. [polars.read_excel](#polarsread_excel)
2. [polars.DataFrame.write_excel](#polarsdataframewrite_excel)


# polars.read_excel

polars.**read_excel**(
    source: str | BytesIO | Path | BinaryIO | bytes, *, 
    sheet_id: None = None, 
    sheet_name: str, 
    xlsx2csv_options: dict[str, Any] | None = None, 
    read_csv_options: dict[str, Any] | None = None
) → DataFrame[source]

polars.**read_excel**(
    
    source: str | BytesIO | Path | BinaryIO | bytes, *, 
    sheet_id: None = None, 
    sheet_name: None = None, 
    xlsx2csv_options: dict[str, Any] | None = None, 
    read_csv_options: dict[str, Any] | None = None
) → DataFrame

polars.**read_excel**(
    
    source: str | BytesIO | Path | BinaryIO | bytes, *, 
    sheet_id: int, 
    sheet_name: str, 
    xlsx2csv_options: dict[str, Any] | None = None, 
    read_csv_options: dict[str, Any] | None = None
) → NoReturn

polars.**read_excel**(
    source: str | BytesIO | Path | BinaryIO | bytes, *, 
    sheet_id: Literal[0], 
    sheet_name: None = None, 
    xlsx2csv_options: dict[str, Any] | None = None, 
    read_csv_options: dict[str, Any] | None = None
) → dict[str, DataFrame]

polars.**read_excel**(
    
    source: str | BytesIO | Path | BinaryIO | bytes, *, 
    sheet_id: int, 
    sheet_name: None = None, 
    xlsx2csv_options: dict[str, Any] | None = None, 
    read_csv_options: dict[str, Any] | None = None
) → DataFrame

Считайте таблицу Excel (XLSX) во фрейм данных.

Преобразует лист Excel с помощью `xlsx2csv.Xlsx2csv().convert()` в CSV и анализирует выходные данные CSV с помощью read_csv().

### Параметры:

**source**

Путь к файлу или файлоподобному объекту. Под файлоподобным объектом мы подразумеваем объекты с методом read(), такие как обработчик файла (например, через встроенную функцию `open`) или `BytesIO`.

**sheet_id**

Номер листа для преобразования (0 для всех листов). Значение по умолчанию равно 1, если не указано ни это, ни `sheet_name`.

**sheet_name**

Название листа для преобразования. Не может использоваться в сочетании с `sheet_id`.

**xlsx2csv_options**

Дополнительные параметры, переданные в `xls2csv.Xlsx2csv()`. например: `{"skip_empty_lines": True}`

**read_csv_options**

Дополнительные параметры, переданные read_csv() для анализа CSV-файла, возвращаемого `xlsx2csv.Xlsx2csv().convert()`, например: `{"has_header": False, "new_columns": ["a", "b", "c"], "infer_schema_length":  None}`

**Returns:** DataFrame

Примеры:

Считайть лист ”My Datasheet" из файла листа Excel во фрейм данных.

```
pl.read_excel(
    "test.xlsx",
    sheet_name="My Datasheet",
)  
```

Считайте лист 3 из файла листа Excel во фрейм данных, пропуская пустые строки на листе. Поскольку на листе 3 нет строки заголовка, передайте необходимые настройки в read_csv().

```
pl.read_excel(
    "test.xlsx",
    sheet_id=3,
    xlsx2csv_options={"skip_empty_lines": True},
    read_csv_options={"has_header": False, "new_columns": ["a", "b", "c"]},
)  
```

Если правильные типы данных не могут быть определены с помощью polars, ознакомьтесь с документацией [read_csv()](#polars.read_csv), чтобы узнать, какие параметры вы можете передать, чтобы устранить эту проблему. Например, `"infer_schema_length": None` можно использовать для чтения всех данных дважды, один раз для вывода правильных выходных типов и один раз для фактического преобразования входных данных в правильные типы. При `“infer_schema_length”: 1000` дважды считываются только первые 1000 строк.

```
pl.read_excel(
    "test.xlsx",
    read_csv_options={"infer_schema_length": None},
)  
If read_excel() does not work or you need to read other types of spreadsheet files, you can try pandas pd.read_excel() (supports xls, xlsx, xlsm, xlsb, odf, ods and odt).

pl.from_pandas(pd.read_excel("test.xlsx"))  
```

# polars.DataFrame.write_excel

DataFrame.**write_excel**(
    
    workbook: Workbook | BytesIO | Path | str | None = None, 
    worksheet: str | None = None, *, 
    position: tuple[int, int] | str = 'A1', 
    table_style: str | dict[str, Any] | None = None, 
    table_name: str | None = None, 
    column_formats: dict[str | tuple[str, ...], str | dict[str, str]] | None = None, 
    dtype_formats: dict[OneOrMoreDataTypes, str] | None = None, 
    conditional_formats: ConditionalFormatDict | None = None, 
    column_totals: ColumnTotalsDefinition | None = None, 
    column_widths: dict[str | tuple[str, ...], int] | int | None = None, 
    row_totals: RowTotalsDefinition | None = None, 
    row_heights: dict[int | tuple[int, ...], int] | int | None = None, 
    sparklines: dict[str, Sequence[str] | dict[str, Any]] | None = None, 
    formulas: dict[str, str | dict[str, str]] | None = None, 
    float_precision: int = 3, 
    has_header: bool = True, 
    autofilter: bool = True, 
    autofit: bool = False, 
    hidden_columns: Sequence[str] | None = None, 
    hide_gridlines: bool = False, 
    sheet_zoom: int | None = None
) → Workbook[source]

Запишите данные фрейма в таблицу в Excel книге/рабочем листе.

### Параметры:

**workbook:** *Workbook*

Строковое имя или путь к создаваемой рабочей книге, объекту BytesIO для записи в него или открытому объекту `xlsxwriter.Workbook`, который не был закрыт. Если один, то записывает в `dataframe.xlsx `рабочая книга в рабочем каталоге.

**worksheet:** *str*

Имя целевого листа; если нет, то при создании новой рабочей книги выполняется запись в `“Sheet1”` (обратите внимание, что для записи в существующую рабочую книгу требуется действительное имя существующего или нового рабочего листа).

**position:** *{str, tuple}*

Позиция таблицы в обозначениях Excel (например: “A1”) или целочисленный кортеж (строка, столбец).

**table_style:** *{str, dict}*

Именованный стиль таблицы Excel, такой как “Table Style Medium 4”, или словарь параметров `{"key":value,}`, содержащий один или несколько из следующих ключей: `“style”`, `“first_column”`, `“last_column”`, `“banded_columns“`, `"banded_rows”`.

**table_name:** *str*

Имя объекта выходной таблицы на рабочем листе; воследствии на него можно ссылаться на листе с помощью формул/диаграмм или с помощью последующих операций xlsxwriter.

**column_formats:** *dict*

Словарь `{colname:str,}` для применения строки формата Excel к заданным столбцам. Форматы, определенные здесь (такие как `“dd/mm/yyyy”, “0.00%”` и т.д.), будут переопределять любые, определенные в `dtype_formats` (далее).

**dtype_formats:** *dict*

Словарь `{dtype:str,}`, который устанавливает формат Excel по умолчанию для данного типа. (Это может быть переопределено для каждого столбца параметром `column_formats`). Также допустимо использовать группы `dtype`, такие как `pl.FLOAT_DTYPES`, в качестве  `dtype/format key`, чтобы упростить настройку единообразных целочисленных форматов и форматов с плавающей точкой.

**conditional_formats:** *dict*

Словарь `{colname(s):str,}`, `{colname(s):dict,} `или `{colname(s):list,}`, определяющий параметры условного формата для указанных столбцов.

При указании строкового имени типа должен быть один из допустимых типов xlsxwriter, таких как `“3_color_scale”`, `“data_bar”` и т.д.

При предоставлении словаря вы можете использовать любые / все поддерживаемые xlsxwriter опции, включая наборы значков, формулы и т.д.

Предоставление нескольких столбцов в качестве кортежа/ключа приведет к применению единого формата ко всем столбцам - это эффективно при создании тепловой карты, поскольку минимальные/максимальные значения будут определяться по всему диапазону, а не для каждого столбца.

Наконец, вы также можете предоставить список, составленный из приведенных выше опций, чтобы применить более одного условного формата к одному и тому же диапазону.

**column_totals:** *{bool, list, dict}*

Добавьте строку с итогом по столбцу в экспортируемую таблицу.

Если значение True, то все числовые столбцы будут иметь соответствующую сумму, используя `“sum”`.

При передаче строки это должно быть одно из допустимых имен функции `total`, и все числовые столбцы будут иметь соответствующую сумму, используя эту функцию.

При передаче списка `colnames` только те, которые указаны, будут иметь общее значение.

Для большего контроля передайте `{colname:funcname,} dict`.

Допустимыми именами функций total являются `“average”, “count_nums”, “count”, “max”, “min”, “std_dev”, “sum” и “var”`.

**column_widths:** *{dict, int}*

`{colname:int,} dict` или одно целое число, которое устанавливает (или переопределяет при автоматической установке) ширину столбцов таблицы в целых пиксельных единицах. Если задано как целое число, то для всех столбцов таблицы используется одно и то же значение.

**row_totals:** *{dict, bool}*

Добавьте столбец "Общее количество строк" в правую часть экспортируемой таблицы.

Если значение `True`, в конце таблицы будет добавлен столбец с именем `“total”`, который применяет функцию `“sum”` по строкам ко всем числовым столбцам.

При передаче списка/последовательности имен столбцов в сумме будут участвовать только совпадающие столбцы.

Можно также передать словарь `{colname:columns,}`, чтобы создать один или несколько итоговых столбцов с разными именами, ссылающихся на разные столбцы.

**row_heights:** *{dict, int}*

`int` или словарь `{row_index:int,}`, который задает высоту заданных строк (если предоставляется словарь) или всех строк (если предоставляется целое число), которые пересекаются с телом таблицы (включая любой заголовок и общую строку) в целых пиксельных единицах. Обратите внимание, что `row_index` начинается с нуля и будет строкой заголовка (если только значение `has_headers` не равно `False`).

**sparklines:** *dict*

Словарь `{colname:list,}` или `{colname:dict,}`, определяющий одну или несколько спарклайнов, которые будут записаны в новый столбец таблицы.

Для большего контроля может быть предоставлен `options dict` для `xlsxwriter-compliant`, и в этом случае доступны три дополнительных ключа, специфичных для polars: `“columns”, “insert_before” и “insert_after”`. Они позволяют вам определить исходные столбцы и расположить спарклайны относительно других столбцов таблицы. Если директива `position` не задана, спарклайны добавляются в конец таблицы (например, в крайний правый угол) в том порядке, в котором они указаны.

**formulas:** *dict*

Словарь `{colname:formula,}` или `{colname:dict,}`, определяющий одну или несколько формул, которые будут записаны в новый столбец таблицы. Обратите внимание, что вам настоятельно рекомендуется использовать структурированные ссылки в ваших формулах везде, где это возможно, чтобы упростить обращение к столбцам по имени.

При указании строковой формулы (например, `“=[@colx]*[@coly]”`) столбец будет добавлен в конец таблицы (например, в крайний правый угол), после любых спарклайнов по умолчанию и перед любыми `row_totals`.

Для большей части управления предоставьте словарь параметров со следующими ключами: `“formula”`  (обязательно), один из `“insert_before”` или `“insert_after”` и необязательно `“return_dtype”`. Последнее используется для надлежащего форматирования выходных данных формулы и позволяет ей участвовать в итоговых значениях строк/столбцов.

**float_precision:** *{dict, int}*

Количество десятичных знаков по умолчанию, отображаемое для столбцов с плавающей запятой (обратите внимание, что это чисто директива форматирования; фактические значения не округляются).

**has_header:** *bool*

Укажите, следует ли создавать таблицу со строкой заголовка.

**autofilter:** *bool*

Если в таблице есть заголовки, обеспечьте возможность автофильтра.

**autofit:** *bool*

Рассчитайте ширину отдельных столбцов на основе полученных данных.

**hidden_columns:** *list*

Список столбцов таблицы, которые нужно скрыть на рабочем листе.

**hide_gridlines:** *bool*

Не отображайте никаких линий сетки на выходном листе.

**sheet_zoom:** *int*

Установите уровень масштабирования выходного листа по умолчанию.

Notes

Словари условного форматирования должны предоставлять определения, совместимые с xlsxwriter; polars позаботится о том, как они применяются на рабочем листе относительно относительного положения листа/столбца. Для получения информации о поддерживаемых параметрах смотрите: [ссылка](https://xlsxwriter.readthedocs.io/working_with_conditional_formats.html)

Аналогично, словари параметров `sparkline` должны содержать ключ/значения, совместимые с `xlsxwriter`, а также обязательный ключ polars `“columns”`, который определяет исходные данные `sparkline`; все эти исходные столбцы должны быть смежными. Доступны два других ключа, специфичных для polars, которые помогают определить, где в таблице появляется спарклайн: `“insert_after”` и `“insert_before”`. Значением, связанным с этими ключами, должно быть имя столбца в экспортируемой таблице.  [ссылка](https://xlsxwriter.readthedocs.io/working_with_sparklines.html)

Словари формул должны содержать ключ с именем `“formula”`, а затем необязательные ключи `“insert_after”, “insert_before”` и/или `“return_dtype”`. Эти дополнительные ключи позволяют вводить столбец в таблицу в определенном месте и/или определять тип возвращаемого значения формулы (например: `“Int64”`, `“Float64”` и т.д.). Формулы, которые ссылаются на столбцы таблицы, должны использовать синтаксис структурированных ссылок Excel, чтобы гарантировать, что формула применяется правильно и относится к таблице. [ссылка](https://support.microsoft.com/en-us/office/using-structured-references-with-excel-tables-f5ed2452-2337-4f71-bed3-c8ae6d2b276e)

Примеры:

Создание экземпляра базового фрейма данных:

```
from random import uniform
from datetime import date

df = pl.DataFrame(
    {
        "dtm": [date(2023, 1, 1), date(2023, 1, 2), date(2023, 1, 3)],
        "num": [uniform(-500, 500), uniform(-500, 500), uniform(-500, 500)],
        "val": [10_000, 20_000, 30_000],
    }
)
```

Экспорт в `“dataframe.xlsx ”` (имя рабочей книги по умолчанию, если не указано) в рабочем каталоге добавьте итоговые значения столбцов (`“sum”`) для всех числовых столбцов, автоматически установите:

```
df.write_excel(column_totals=True, autofit=True)  
```

Запишите фрейм в определенное место на листе, установите именованный стиль таблицы, примените форматирование даты в US-стиле, увеличьте точность с плавающей запятой по умолчанию, примените функцию итога, отличную от стандартной, к одному столбцу, автоподстройка:


```
df.write_excel(  
    position="B4",
    table_style="Table Style Light 16",
    dtype_formats={pl.Date: "mm/dd/yyyy"},
    column_totals={"num": "average"},
    float_precision=6,
    autofit=True,
)
```

Дважды запишите один и тот же фрейм на именованный рабочий лист, применяя разные стили и условное форматирование к каждой таблице, добавляя заголовки таблиц с помощью явной интеграции xlsxwriter:

```
from xlsxwriter import Workbook
with Workbook("multi_frame.xlsx") as wb:  
    # basic/default conditional formatting
    df.write_excel(
        workbook=wb,
        worksheet="data",
        position=(3, 1),  # укажите позицию в виде координат (строка, столбец)
        conditional_formats={"num": "3_color_scale", "val": "data_bar"},
        table_style="Table Style Medium 4",
    )

    # расширенное условное форматирование, пользовательский стиль
    df.write_excel(
        workbook=wb,
        worksheet="data",
        position=(len(df) + 7, 1),
        table_style={
            "style": "Table Style Light 4",
            "first_column": True,
        },
        conditional_formats={
            "num": {
                "type": "3_color_scale",
                "min_color": "#76933c",
                "mid_color": "#c4d79b",
                "max_color": "#ebf1de",
            },
            "val": {
                "type": "data_bar",
                "data_bar_2010": True,
                "bar_color": "#9bbb59",
                "bar_negative_color_same": True,
                "bar_negative_border_color_same": True,
            },
        },
        column_formats={"num": "#,##0.000;[White]-#,##0.000"},
        column_widths={"val": 125},
        autofit=True,
    )

    # добавьте несколько заголовков таблиц (в пользовательском формате)
    ws = wb.get_worksheet_by_name("data")
    fmt_title = wb.add_format(
        {
            "font_color": "#4f6228",
            "font_size": 12,
            "italic": True,
            "bold": True,
        }
    )
    ws.write(2, 1, "Basic/default conditional formatting", fmt_title)
    ws.write(len(df) + 6, 1, "Customised conditional formatting", fmt_title)
```

Экспортируйте таблицу, содержащую два разных типа спарклайнов. Используйте параметры по умолчанию для спарклайна `“trend”` и настраиваемые параметры (и позиционирование) для спарклайна `“+/-” win_loss` с форматированием целочисленного типа по умолчанию, итогами по столбцам, тонкой двухцветной тепловой картой и скрытыми линиями сетки рабочего листа:

```
df = pl.DataFrame(
    {
        "id": ["aaa", "bbb", "ccc", "ddd", "eee"],
        "q1": [100, 55, -20, 0, 35],
        "q2": [30, -10, 15, 60, 20],
        "q3": [-50, 0, 40, 80, 80],
        "q4": [75, 55, 25, -10, -55],
    }
)
df.write_excel(  
    table_style="Table Style Light 2",
    # примените формат ко всем вариантам integer
    dtype_formats={pl.INTEGER_DTYPES: "#,##0_);(#,##0)"},
    sparklines={
        # параметры по умолчанию; просто укажите исходные столбцы
        "trend": ["q1", "q2", "q3", "q4"],
        # индивидуальный тип спарклайна с директивой позиционирования
        "+/-": {
            "columns": ["q1", "q2", "q3", "q4"],
            "insert_after": "id",
            "type": "win_loss",
        },
    },
    conditional_formats={
        # создайте единую многоколоночную тепловую карту
        ("q1", "q2", "q3", "q4"): {
            "type": "2_color_scale",
            "min_color": "#95b3d7",
            "max_color": "#ffffff",
        },
    },
    column_totals=["q1", "q2", "q3", "q4"],
    row_totals=True,
    hide_gridlines=True,
)
```

Экспортируйте таблицу, содержащую столбец на основе формулы Excel, который вычисляет стандартизированный Z-score, показывая использование структурированных ссылок в сочетании с директивами позиционирования, итоговыми значениями столбцов и пользовательским форматированием.

```
df = pl.DataFrame(
    {
        "id": ["a123", "b345", "c567", "d789", "e101"],
        "points": [99, 45, 50, 85, 35],
    }
)
df.write_excel(  
    table_style={
        "style": "Table Style Medium 15",
        "first_column": True,
    },
    column_formats={
        "id": {"font": "Consolas"},
        "points": {"align": "center"},
        "z-score": {"align": "center"},
    },
    column_totals="average",
    formulas={
        "z-score": {
            # используйте структурированные ссылки для ссылок на столбцы таблицы и строку "totals"
            "formula": "=STANDARDIZE([@points], [[#Totals],[points]], STDEV([points]))",
            "insert_after": "points",
            "return_dtype": pl.Float64,
        }
    },
    hide_gridlines=True,
    sheet_zoom=125,
)
```