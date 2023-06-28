# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2023-06-28
### Added
- Test coverage badge to README.
- Daily testing in CI.
- List optional dependencies given in pyproject.toml.
### Changed
- Remove text warning about this software being an early prototype.
- Fix bad comments in flake8 config section causing flake8 6.0.0  runs to error.
- Switch package build system from setuptools to hatch.

## [0.2.0] - 2022-03-25
### Added
- Type annotations and mypy testing in CI.
### Removed
- `DtrRun` has been removed. Support for DTR files has been dropped.
