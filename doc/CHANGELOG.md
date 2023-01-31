# Changelog
All notable changes to this project will be documented in this file.
 - `Added` for new features.
 - `Changed` for changes in existing functionality.
 - `Deprecated` for soon-to-be removed features.
 - `Removed` for now removed features.
 - `Fixed` for any bug fixes.
 - `Security` in case of vulnerabilities.
<hr>
 

## Upcoming features
 - ~~Add [iterparse](https://stackoverflow.com/questions/53445280/python-lxml-iterparse-is-skipping-first-event) in XmlParser for parsing large files~~ (not possible; cannot iterate through nodes from root up)
 - Add a method on fileparser that defines a tables structure -> retrieve data types
 - Add init methods to all submodules
 - separate py files in module root into their own submodules
 - Cythonize `Parser`
 - Cythonize `Structure`, `Node`
<hr>

## 2022-05-04
### Added
- `Node` added structure_id property
- `Node` added id property
### Changed
- `flatten function` - specify links between tables -> add table name to foreign key column like `[node_tagpath]_id`?
### Removed
- `Node` __create_id method (replaced by id property)
<hr>


## 2022-05-04
### Added
- Added version, author etc to init and modified setup.py to use these values
- Structure has 'summarize' attribute
- added summarize argument to parser.parse methods
- added `Structure.get_node_by_id`
- `display_structure_difference` colored difference between two files -> create structure compare
### Changed
- `Parser.parse` now returns `Structure` instance instead of setting it as an attribute in the `Parser` class
- `Parser.get_signature` is now indifferent of the order of tags. Signature is created based on the path and count of the element in the structure
### Removed
- removed set_summarize attribute from `FileParser` (and subclasses)
- summarize attribute from `FileParser` (and subclasses)
### Fixed
- `Structure.format_structure` 
<hr>



## 2022-05-03
### Added
- Added changelog 
- Added get_signature to Structure
### Fixed
- flatten function now sets index as foreign key
<hr>

