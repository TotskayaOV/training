# Input/output
## [CSV](./file_csv.md)
| функция | краткое описание |
|----------|------------------|
|`read_csv(source, *[, has_header, columns, ...])` | Считать файл .csv в фрейм данных |
|`scan_csv(source, *[, has_header, separator, ...])`| Lazily-считывание одного .csv файла или нескольких файлов с помощью глобального шаблона|
|`DataFrame.write_csv()`| запись в файл .csv значений (разделитель ',') |

## Feather/ IPC
| функция | краткое описание |
|----------|------------------|
|`read_ipc(source, *[, columns, n_rows, ...])` | Считать файл Arrow IPC (Feather v2) в фрейм данных |
|`scan_ipc(source, *[, n_rows, cache, ...])`| Lazily-считывание одного Arrow IPC (Feather v2) файла или нескольких файлов с помощью глобального шаблона|
|`read_ipc_schema(source)`| получить схему из файла IPC без чтения данных|
|`DataFrame.write_ipc()`| запись в двоичный поток Arrow IPC или файл Feather. |

## Parquet
| функция | краткое описание |
|----------|------------------|
|`read_parquet(source, *[, columns, n_rows, ...])` | Считать файл parquet в фрейм данных |
|`scan_parquet(source, *[, n_rows, cache, ...])`| Lazily-считывание одного parquet файла или нескольких файлов с помощью глобального шаблона|
|`read_parquet_schema(source)`| получить схему из файла parquet без чтения данных|
|`DataFrame.write_parquet(file, *[, ...])`| запись в  файл Apache Parquet |

## Database
| функция | краткое описание |
|----------|------------------|
|`read_database(query, connection_uri, *[, ...])` | Считайте SQL-запрос во фрейм данных |
|`DataFrame.write_database(table_name, ...[, ...])`| запись фрейм polars в базу данных |

## JSON
| функция | краткое описание |
|----------|------------------|
|`read_json(source)` | Считать файл JSON в фрейм данных |
|`read_ndjson(source)` | Считать файл JSON в фрейм данных (разделитель - новая строка) |
|`scan_ndjson(source, *[, ...])`| Lazily-считывание одного JSON файла или нескольких файлов с помощью глобального шаблона (разделитель - новая строка)|
|`DataFrame.write_json()`| запись в JSON файл |
|`DataFrame.write_ndjson()`| запись в JSON файл (разделитель - новая строка) |

## AVRO
| функция | краткое описание |
|----------|------------------|
|`read_avro(source, *[, columns, n_rows])` | Считывает во фрейм данных из формата Apache Avro |
|`DataFrame.write_database(table_name, ...[, ...])`| запись в формат Apache Avro |

## [Excel](./excel.md)
| функция | краткое описание |
|----------|------------------|
|`read_excel()` | Считывает во фрейм данных из Excel (XLSX) |
|`DataFrame.write_excel([workbook, worksheet, ...])`| запись фрема данных в таблицу Excel [книга, лист, ...] |

## Delta Lake
| функция | краткое описание |
|----------|------------------|
|`read_delta(source, *[, version, columns, ...])` | Считать таблицу Delta lake в фрейм данных |
|`scan_delta(source, *[, version, ...])`| Lazily-считывание таблицы Delta lake |
|`DataFrame.write_delta(target, *[, mode, ...])`| запись в таблицу Delta Lake фрейма данных |

## Datasets
Подключитесь к pyarrow datasets
| функция | краткое описание |
|----------|------------------|
|`scan_pyarrow_dataset(source, *[, ...])` | Считать данные pyarrow |

## [BatchedCsvReader]((./file_csv.md))
Этот считыватель становится доступным при вызове pl.read_csv_batched
| функция | краткое описание |
|----------|------------------|
|`BatchedCsvReader.next_batches(n)` | считать n-пакетов |

[Источник](https://pola-rs.github.io)