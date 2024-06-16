install:
	poetry install

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user --force-reinstall dist/*.whl

lint:
	poetry run flake8 gendiff

check:
	poetry check
# Команда poetry check используется для проверки файла pyproject.toml
# и установленных зависимостей на правильность.
# all set! означает, что конфигурационный файл в порядке и все зависимости успешно прошли проверку.
# Это позволяет гарантировать правильность настроек проекта и его зависимостей перед началом работы.

test-coverage:
	poetry run pytest --cov=gendiff --cov-report xml

test:
	poetry run pytest

test-cov:
	poetry run pytest --cov