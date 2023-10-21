1. [polars.read_csv](#polarsread_csv)
2. [polars.read_csv_batched](#polarsread_csv_batched)
3. [polars.scan_csv](#polarsscan_csv)
4. [polars.DataFrame.write_csv](#polarsdataframewrite_csv)


# polars.read_csv
polars.**read_csv**(

        source: str | TextIO | BytesIO | Path | BinaryIO | bytes, *, 
        has_header: bool = True, 
        columns: Sequence[int] | Sequence[str] | None = None, 
        new_columns: Sequence[str] | None = None, 
        separator: str = ',', 
        comment_char: str | None = None, 
        quote_char: str | None = '"', 
        skip_rows: int = 0, 
        dtypes: Mapping[str, PolarsDataType] | Sequence[PolarsDataType] | None = None, 
        null_values: str | Sequence[str] | dict[str, str] | None = None, 
        missing_utf8_is_empty_string: bool = False, 
        ignore_errors: bool = False, 
        try_parse_dates: bool = False, 
        n_threads: int | None = None, 
        infer_schema_length: int | None = 100, 
        batch_size: int = 8192, 
        n_rows: int | None = None, 
        encoding: CsvEncoding | str = 'utf8', 
        low_memory: bool = False, 
        rechunk: bool = True, 
        use_pyarrow: bool = False, 
        storage_options: dict[str, Any] | None = None, 
        skip_rows_after_header: int = 0, 
        row_count_name: str | None = None, 
        row_count_offset: int = 0, 
        sample_size: int = 1024, 
        eol_char: str = '\n'
    ) → DataFrame[source]

Чтение файла .csv в фрейм данных.

### Параметры:
**source**

Путь к файлу или файлоподобному объекту. Под файлоподобным объектом мы подразумеваем объекты с методом `read()`, такие как обработчик файла (например, через встроенную функцию `open`) или `StringIO` или `BytesIO`. Если установлен `fsspec`, он будет использоваться для открытия удаленных файлов.

**has_header**

Укажите, является ли первая строка набора данных заголовком или нет. Если установлено значение `False`, имена столбцов будут автоматически сгенерированы в следующем формате: `column_x`, где `x` является перечислением для каждого столбца в наборе данных, начиная с 1.

**columns**

Столбцы для выбора. Принимает список индексов столбцов (начиная с нуля) или список имен столбцов.

**new_columns**

Переименуйте столбцы сразу после разбора CSV-файла. Если данный список короче ширины фрейма данных, то остальные столбцы будут иметь свое первоначальное название.

**separator**

Разделитель

**comment_char**

Символ, указывающий на начало строки комментария, например `#`.

**quote_char**

Символ, используемый для цитирования в формате .csv, по умолчанию = `"`. Установите значение `None`, чтобы отключить специальную обработку и экранирование кавычек

**skip_rows**

Начать чтение со строки `skip_rows`

**dtypes**

Перезаписывать типы для определенных или всех столбцов во время вывода схемы.  

**null_values**

Значения для интерпретации как нулевые значения. Можно задать:

* `str`: Все значения, равные этой строке, будут равны null.
* `List[str]`: Все значения, равные любой строке в этом списке, будут равны null.
* `Dict[str, str]`: Словарь, который сопоставляет имя столбца со строкой нулевого значения.

**missing_utf8_is_empty_string**

По умолчанию пропущенное значение считается равным `null`; если вы предпочитаете, чтобы пропущенные значения `utf-8` рассматривались как пустая строка, вы можете установить этому параметру значение `True`.

**ignore_errors**

Будет пытаться продолжать читать строки, если в некоторых строках возникают ошибки. Перед использованием этой опции попробуйте увеличить количество строк, используемых для вывода схемы, например, `infer_schema_length=10000`, или переопределить автоматический вывод `dtype` для определенных столбцов с помощью параметра `dtypes`, или используйте `infer_schema_length=0`, чтобы прочитать все столбцы как `pl.Utf8`, чтобы проверить, какие значения могут вызвать проблему.

**try_parse_dates**

Попробуйте автоматически анализировать даты. Можно вывести большинство форматов, подобных `ISO8601`, а также несколько других. Если это не удается, столбец остается с типом данных `pl.Utf 8`. 

Если `use_pyarrow=True`, даты всегда будут анализироваться.

**n_threads**

Количество потоков, используемых при разборе csv. По умолчанию используется количество физических процессоров вашей системы.

**infer_schema_length**

Максимальное количество строк, которые необходимо прочитать для вывода схемы. Если схема выведена неправильно (например, как `pl.Int64` вместо `pl.Float64`), попробуйте увеличить количество строк, используемых для вывода схемы, или переопределить выведенный `dtype` для этих столбцов с `dtypes`. Если установлено значение 0, все столбцы будут считываться как `pl.Utf 8`. Если установлено значение `None`, будет выполнено полное сканирование таблицы (медленно).

**batch_size**

Количество строк, считываемых в буфер за один раз. Измените это, чтобы изменить производительность.

**n_rows**

Прекратитm чтение из CSV-файла после прочтения `n_rows`. Во время многопоточного синтаксического анализа верхняя граница строк `n_rows `не может быть гарантирована.

**encoding** *{‘utf8’, ‘utf8-lossy’, …}*

С потерями означает, что недопустимые значения `utf8` заменяются символами �. При использовании других кодировок, отличных от `utf8` или `utf8-lossy`, входные данные сначала декодируются в памяти с помощью python. По умолчанию используется `utf8`.   

**low_memory**

Сократить использование памяти за счет снижения производительности.

**rechunk**

Убедитесь, что все столбцы являются смежными в памяти, объединив фрагменты в единый массив.

**use_pyarrow**

Попробовать использовать собственный CSV-анализатор pyarrow. Всегда будет анализировать даты, даже если `try_parse_dates=False`. Это не всегда возможно. Набор аргументов, передаваемых этой функции, определяет, возможно ли использовать собственный синтаксический анализатор pyarrow. Обратите внимание, что у yarrow и polars может быть разная стратегия в отношении вывода типа данных.

**storage_options**

Дополнительные параметры, которые имеют смысл для `fsspec.open()` или конкретного подключения к хранилищу. например, хост, порт, имя пользователя, пароль и т.д.

**skip_rows_after_header**

Пропустить это количество строк при разборе заголовка.

**row_count_name**

Если не None, то это приведет к вставке столбца количества строк с заданным именем во фрейм данных. 

**row_count_offset**

Смещение для начала столбца `row_count` (используется только в том случае, если задано имя).

**sample_size**

Установите размер выборки. Используется для выборки статистических данных для оценки необходимого распределения.

**eol_char**

Символ конца строки

**Returns:** DataFrame.

*По умолчанию rechank выполняется в виде фрагмента в конце, что означает, что все данные будут непрерывно храниться в памяти. Установите rechunk=False, если вы проводите сравнительный анализ чтения csv. Rechank - дорогостоящая операция.*

# polars.read_csv_batched

polars.**read_csv_batched**(
        
        source: str | Path, *, 
        has_header: bool = True, 
        columns: Sequence[int] | Sequence[str] | None = None, 
        new_columns: Sequence[str] | None = None, 
        separator: str = ',', 
        comment_char: str | None = None, 
        quote_char: str | None = '"', 
        skip_rows: int = 0, 
        dtypes: Mapping[str, PolarsDataType] | Sequence[PolarsDataType] | None = None, 
        null_values: str | Sequence[str] | dict[str, str] | None = None, 
        missing_utf8_is_empty_string: bool = False, 
        ignore_errors: bool = False, 
        try_parse_dates: bool = False, 
        n_threads: int | None = None, 
        infer_schema_length: int | None = 100, 
        batch_size: int = 50000, 
        n_rows: int | None = None, 
        encoding: CsvEncoding | str = 'utf8', 
        low_memory: bool = False, 
        rechunk: bool = True, 
        skip_rows_after_header: int = 0, 
        row_count_name: str | None = None, 
        row_count_offset: int = 0, 
        sample_size: int = 1024, 
        eol_char: str = '\n'
    ) → BatchedCsvReader[source]

Чтение файла .csv в пактеном режиме

После создания `BatchedCsvReader` Polars соберет статистику и определит фрагменты файла. После этого работа будет выполнена только в том случае, если будет вызван `next_batches`.

### Параметры:
**source**

Путь к файлу или файлоподобному объекту. Под файлоподобным объектом мы подразумеваем объекты с методом `read()`, такие как обработчик файла (например, через встроенную функцию `open`) или `StringIO` или `BytesIO`. Если установлен `fsspec`, он будет использоваться для открытия удаленных файлов.

**has_header**

Укажите, является ли первая строка набора данных заголовком или нет. Если установлено значение `False`, имена столбцов будут автоматически сгенерированы в следующем формате: `column_x`, где `x` является перечислением для каждого столбца в наборе данных, начиная с 1.

**columns**

Столбцы для выбора. Принимает список индексов столбцов (начиная с нуля) или список имен столбцов.

**new_columns**

Переименуйте столбцы сразу после разбора CSV-файла. Если данный список короче ширины фрейма данных, то остальные столбцы будут иметь свое первоначальное название.

**separator**

Разделитель

**comment_char**

Символ, указывающий на начало строки комментария, например `#`.

**quote_char**

Символ, используемый для цитирования в формате .csv, по умолчанию = "``. Установите значение None, чтобы отключить специальную обработку и экранирование кавычек

**skip_rows**

Начать чтение со строки `skip_rows`

**dtypes**

Перезаписывать типы для определенных или всех столбцов во время вывода схемы.  

**null_values**

Значения для интерпретации как нулевые значения. Можно задать:

* `str`: Все значения, равные этой строке, будут равны `null`.
* `List[str]`: Все значения, равные любой строке в этом списке, будут равны null.
* `Dict[str, str]`: Словарь, который сопоставляет имя столбца со строкой нулевого значения.

**missing_utf8_is_empty_string**

По умолчанию пропущенное значение считается равным `null`; если вы предпочитаете, чтобы пропущенные значения `utf-8` рассматривались как пустая строка, вы можете установить этому параметру значение `True`.

**ignore_errors**

Будет пытаться продолжать читать строки, если в некоторых строках возникают ошибки. Перед использованием этой опции попробуйте увеличить количество строк, используемых для вывода схемы, например, `infer_schema_length=10000`, или переопределить автоматический вывод `dtype` для определенных столбцов с помощью параметра `dtypes`, или используйте `infer_schema_length=0`, чтобы прочитать все столбцы как `pl.Utf8`, чтобы проверить, какие значения могут вызвать проблему.

**try_parse_dates**

Попробуйте автоматически анализировать даты. Можно вывести большинство форматов, подобных `ISO8601`, а также несколько других. Если это не удается, столбец остается с типом данных `pl.Utf 8`. 
    
Если `use_pyarrow=True`, даты всегда будут анализироваться.

**n_threads**

Количество потоков, используемых при разборе csv. По умолчанию используется количество физических процессоров вашей системы.

**ignore_errors**

Старайтесь продолжать читать строки, если в некоторых строках возникают ошибки. Сначала попробуйте `infer_schema_length=0`, чтобы прочитать все столбцы как `pl.Utf8`, чтобы проверить, какие значения могут вызвать проблему.

**try_parse_dates**

Попробовать автоматически анализировать даты. Можно вывести большинство форматов, подобных `ISO8601`, а также несколько других. Если это не удается, столбец остается с типом данных `pl.Utf 8`.

**n_threads**

Количество потоков, используемых при разборе csv. По умолчанию используется количество физических процессоров вашей системы.

**infer_schema_length**

Максимальное количество строк, которые необходимо прочитать для вывода схемы. Если установлено значение 0, все столбцы будут считываться как `pl.Utf 8`. Если установлено значение `None`, будет выполнено полное сканирование таблицы (медленно).

**batch_size**

Количество строк, считываемых в буфер за один раз. 

Измените это, чтобы изменить производительность.

**n_rows**

Прекратить чтение из CSV-файла после прочтения `n_rows`. Во время многопоточного синтаксического анализа верхняя граница строк `n_rows `не гарантируется.

**encoding** *{‘utf8’, ‘utf8-lossy’, …}*

С потерями означает, что недопустимые значения `utf8` заменяются символами �. При использовании других кодировок, отличных от `utf 8` или `utf8-lossy`, входные данные сначала декодируются в памяти с помощью python. По умолчанию используется `utf8`.   

**low_memory**

Сократить использование памяти за счет снижения производительности.

**rechunk**

Убедитесь, что все столбцы являются смежными в памяти, объединив фрагменты в единый массив.

**skip_rows_after_header**

Пропустить количество строк `skip_rows_after_header` при выделении заголовка.

**row_count_name**

Если не None, то это приведет к вставке столбца количества строк с заданным именем во фрейм данных. 

**row_count_offset**

Смещение для начала столбца `row_coun`t (используется только в том случае, если задано имя).

**sample_size**

Установите размер выборки. Используется для выборки статистических данных для оценки необходимого распределения.

**eol_char**

Символ конца строки

**Returns:** DataFrame

*По умолчанию rechank выполняется в виде фрагмента в конце, что означает, что все данные будут непрерывно храниться в памяти. Установите rechunk=False, если вы проводите сравнительный анализ чтения csv. Rechank - дорогостоящая операция.*

```` reader = pl.read_csv_batched(
    "./tpch/tables_scale_100/lineitem.tbl", separator="|", try_parse_dates=True
)  
batches = reader.next_batches(5)  
for df in batches:  
    print(df)
````

Считывайте большой CSV-файл пакетами и записывайте CSV-файл для каждой интересующей вас “группы”.

```` 
seen_groups = set()
reader = pl.read_csv_batched("big_file.csv")  
batches = reader.next_batches(100) 
````

```` 
while batches:  
    df_current_batches = pl.concat(batches)
    partition_dfs = df_current_batches.partition_by("group", as_dict=True)

    for group, df in partition_dfs.items():
        if group in seen_groups:
            with open(f"./data/{group}.csv", "a") as fh:
                fh.write(df.write_csv(file=None, has_header=False))
        else:
            df.write_csv(file=f"./data/{group}.csv", has_header=True)
        seen_groups.add(group)

    batches = reader.next_batches(100) 
````

# polars.scan_csv

polars.**scan_csv**(
    
    source: str | Path, *, 
    has_header: bool = True, 
    separator: str = ',', 
    comment_char: str | None = None, 
    quote_char: str | None = '"', 
    skip_rows: int = 0, 
    dtypes: SchemaDict | Sequence[PolarsDataType] | None = None, 
    null_values: str | Sequence[str] | dict[str, str] | None = None, 
    missing_utf8_is_empty_string: bool = False, 
    ignore_errors: bool = False, 
    cache: bool = True, 
    with_column_names: Callable[[list[str]], list[str]] | None = None, 
    infer_schema_length: int | None = 100, 
    n_rows: int | None = None, 
    encoding: CsvEncoding = 'utf8', 
    low_memory: bool = False, 
    rechunk: bool = True, 
    skip_rows_after_header: int = 0, 
    row_count_name: str | None = None, 
    row_count_offset: int = 0, 
    try_parse_dates: bool = False, 
    eol_char: str = '\n', 
    new_columns: Sequence[str] | None = None
) → LazyFrame[source]

Lazily считывание из файла .csv или нескольких файлов с помощью ukj,глобальных шаблонов.

Это позволяет оптимизатору запросов опускать предикаты и проекции до уровня сканирования, тем самым потенциально снижая нагрузку на память.

### Параметры:
**source**

Путь до файла

**has_header**

Укажите, является ли первая строка набора данных заголовком или нет. Если установлено значение `False`, имена столбцов будут автоматически сгенерированы в следующем формате: `column_x`, где `x` является перечислением для каждого столбца в наборе данных, начиная с 1.

**separator**

Разделитель

**comment_char**

Символ, указывающий на начало строки комментария, например `#`.

**quote_char**

Символ, используемый для цитирования в формате .csv, по умолчанию = "``. Установите значение None, чтобы отключить специальную обработку и экранирование кавычек

**skip_rows**

Начать чтение со строки `skip_rows`

**dtypes**

Перезаписывать типы во время вывода; должно быть `{colname:dtype,} dict` или, если предоставляется список строк для `new_columns`, список `dtypes` одинаковой длины.


**null_values**

Значения для интерпретации как нулевые значения. Можно задать:

* `str`: Все значения, равные этой строке, будут равны `null`.
* `List[str]`: Все значения, равные любой строке в этом списке, будут равны null.
* `Dict[str, str]`: Словарь, который сопоставляет имя столбца со строкой нулевого значения.

**missing_utf8_is_empty_string**

По умолчанию пропущенное значение считается равным `null`; если вы предпочитаете, чтобы пропущенные значения `utf-8` рассматривались как пустая строка, вы можете установить этому параметру значение `True`.

**ignore_errors**

Старайтесь продолжать читать строки, если в некоторых строках возникают ошибки. Сначала попробуйте `infer_schema_length=0`, чтобы прочитать все столбцы как `pl.Utf8`, чтобы проверить, какие значения могут вызвать проблему.

**cache**

Кэшируование результата после прочтения.

**with_column_names**

Применить функцию к именам столбцов точно вовремя (когда они будут определены); эта функция получит (и должна вернуть) список имен столбцов.

**infer_schema_length**

Максимальное количество строк, которые необходимо прочитать для вывода схемы. Если установлено значение 0, все столбцы будут считываться как `pl.Utf 8`. Если установлено значение None, будет выполнено полное сканирование таблицы (медленно).

**n_rows**

Прекратить чтение из CSV-файла после прочтения `n_rows`.

**encoding** *{‘utf8’, ‘utf8-lossy’, …}*

С потерями означает, что недопустимые значения `utf8` заменяются символами �. По умолчанию используется `utf8`.   

**low_memory**

Сократить использование памяти за счет снижения производительности.

**rechunk**

Перераспределить в непрерывную память, когда все фрагменты / файлы будут проанализированы.

**skip_rows_after_header**

Пропустить это количество строк при разборе заголовка.

**row_count_name**

Если не `None`, то это приведет к вставке столбца количества строк с заданным именем во фрейм данных.

**row_count_offset**

Смещение для начала столбца `row_count` (используется только в том случае, если задано имя).

**try_parse_dates**

Попробуйте автоматически анализировать даты. Можно вывести большинство форматов, подобных `ISO8601`, а также несколько других. Если это не удается, столбец остается с типом данных `pl.Utf 8`.

**eol_char**

символ конца строки

**new_columns**

Предоставьте явный список имен строковых столбцов для использования (например, при сканировании CSV-файла без заголовка). Обратите внимание, что в отличие от `read_csv` предоставление меньшего количества имен столбцов, чем имеется в файле, считается ошибкой.

**Returns:** LazyFrame

*Примеры:*

````
import pathlib

(
    pl.scan_csv("my_long_file.csv")  # lazy, doesn't do a thing
    .select(
        ["a", "c"]
    )  # select only 2 columns (other columns will not be read)
    .filter(
        pl.col("a") > 10
    )  # the filter is pushed down the scan, so less data is read into memory
    .fetch(100)  # pushed a limit of 100 rows to the scan level
)  
````

We can use with_column_names to modify the header before scanning:

```
df = pl.DataFrame(
    {"BrEeZaH": [1, 2, 3, 4], "LaNgUaGe": ["is", "hard", "to", "read"]}
)
path: pathlib.Path = dirpath / "mydf.csv"
df.write_csv(path)
pl.scan_csv(
    path, with_column_names=lambda cols: [col.lower() for col in cols]
).collect()
shape: (4, 2)
┌─────────┬──────────┐
│ breezah ┆ language │
│ ---     ┆ ---      │
│ i64     ┆ str      │
╞═════════╪══════════╡
│ 1       ┆ is       │
│ 2       ┆ hard     │
│ 3       ┆ to       │
│ 4       ┆ read     │
└─────────┴──────────┘
`````

You can also simply replace column names (or provide them if the file has none) by passing a list of new column names to the new_columns parameter:

```
df.write_csv(path)
pl.scan_csv(
    path,
    new_columns=["idx", "txt"],
    dtypes=[pl.UInt16, pl.Utf8],
).collect()
shape: (4, 2)
┌─────┬──────┐
│ idx ┆ txt  │
│ --- ┆ ---  │
│ u16 ┆ str  │
╞═════╪══════╡
│ 1   ┆ is   │
│ 2   ┆ hard │
│ 3   ┆ to   │
│ 4   ┆ read │
└─────┴──────┘
````
# polars.DataFrame.write_csv

DataFrame.**write_csv**(
    
    file: None = None, *, 
    has_header: bool = True, 
    separator: str = ',', 
    quote: str = '"', 
    batch_size: int = 1024, 
    datetime_format: str | None = None, 
    date_format: str | None = None, 
    time_format: str | None = None, 
    float_precision: int | None = None, 
    null_value: str | None = None
) → str[source]

DataFrame.**write_csv**(
    
    file: BytesIO | str | Path, *, 
    has_header: bool = True, 
    separator: str = ',', 
    quote: str = '"', 
    batch_size: int = 1024, 
    datetime_format: str | None = None, 
    date_format: str | None = None, 
    time_format: str | None = None, 
    float_precision: int | None = None, 
    null_value: str | None = None
) → None

Запись в файл .csv значений, разделенных запятыми

### Параметры:
**file**

Путь к файлу, в который должен быть записан результат. Если задано значение `None` (по умолчанию), выходные данные вместо этого возвращаются в виде строки.

**has_header**

Следует ли включать заголовок.

**separator**

Разделитель

**quote**

Использовать в качестве символа, заключенного в кавычки.

**batch_size**

Количество строк, которые будут обработаны в каждом потоке.

**datetime_format**

Строка формата со спецификаторами, определенными в chrono Rust crate. Если формат не указан, точность в долях секунды по умолчанию определяется исходя из максимальной временной единицы, найденной в столбцах даты и времени фрейма (если таковые имеются).

**date_format**

Строка формата со спецификаторами, определенными в chrono Rust crate.

**time_format**

Строка формата со спецификаторами, определенными в chrono Rust crate.

**float_precision**

Количество знаков после запятой для записи, применяемое как к типам данных `Float32`, так и к `Float64`.

**null_value**

Строка, представляющая нулевые значения (по умолчанию используется пустая строка).

Пример:

````
import pathlib

df = pl.DataFrame(
    {
        "foo": [1, 2, 3, 4, 5],
        "bar": [6, 7, 8, 9, 10],
        "ham": ["a", "b", "c", "d", "e"],
    }
)
path: pathlib.Path = dirpath / "new_file.csv"
df.write_csv(path, separator=",")
````

[Источник](https://pola-rs.github.io)