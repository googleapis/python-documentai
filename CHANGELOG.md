# Changelog

## [1.0.0](https://www.github.com/googleapis/python-documentai/compare/v0.5.0...v1.0.0) (2021-07-26)


### Features

* add always_use_jwt_access ([35e3b74](https://www.github.com/googleapis/python-documentai/commit/35e3b74474719ef22449fbcb4772e6d381e80874))
* add the processor management methods ([35e3b74](https://www.github.com/googleapis/python-documentai/commit/35e3b74474719ef22449fbcb4772e6d381e80874))
* bump release level to production/stable ([#151](https://www.github.com/googleapis/python-documentai/issues/151)) ([1e6b470](https://www.github.com/googleapis/python-documentai/commit/1e6b470673c4ff71f0f49c11825cb408d1929a88))
* Move CommonOperationMetadata for potential reuse ([#157](https://www.github.com/googleapis/python-documentai/issues/157)) ([a1a92b2](https://www.github.com/googleapis/python-documentai/commit/a1a92b20cc6afa80434a00a90690f1470ed48353))
* update ReviewDocumentRequest to allow set priority and enable validation ([#172](https://www.github.com/googleapis/python-documentai/issues/172)) ([35e3b74](https://www.github.com/googleapis/python-documentai/commit/35e3b74474719ef22449fbcb4772e6d381e80874))
* **v1beta3:** update document.proto, add the processor management methods ([#160](https://www.github.com/googleapis/python-documentai/issues/160)) ([54bc0e9](https://www.github.com/googleapis/python-documentai/commit/54bc0e9c70046bb411dafd53d98c501676585aaf))
* **v1:** Move CommonOperationMetadata into a separate file for potential reuse ([#158](https://www.github.com/googleapis/python-documentai/issues/158)) ([c309f8f](https://www.github.com/googleapis/python-documentai/commit/c309f8f6f88e0308677fc68a7825b3eac7b57627))


### Bug Fixes

* **deps:** add packaging requirement ([#162](https://www.github.com/googleapis/python-documentai/issues/162)) ([f09f807](https://www.github.com/googleapis/python-documentai/commit/f09f8075a3b76fe0d226afa955dae170117df0d0))
* **deps:** pin 'google-{api,cloud}-core', 'google-auth' to allow 2.x versions ([#180](https://www.github.com/googleapis/python-documentai/issues/180)) ([8eab36e](https://www.github.com/googleapis/python-documentai/commit/8eab36e8ff8616ccfdfd4c4149265030bab45d19))
* disable always_use_jwt_access ([35e3b74](https://www.github.com/googleapis/python-documentai/commit/35e3b74474719ef22449fbcb4772e6d381e80874))
* enable self signed jwt for grpc ([#184](https://www.github.com/googleapis/python-documentai/issues/184)) ([1e35b42](https://www.github.com/googleapis/python-documentai/commit/1e35b42739f36d7e1f19528299dac40de5b0cca4))
* exclude docs and tests from package ([#159](https://www.github.com/googleapis/python-documentai/issues/159)) ([1325677](https://www.github.com/googleapis/python-documentai/commit/132567742a2a9927665ed46278952815088ccafc))


### Documentation

* omit mention of Python 2.7 in 'CONTRIBUTING.rst' ([#1127](https://www.github.com/googleapis/python-documentai/issues/1127)) ([#164](https://www.github.com/googleapis/python-documentai/issues/164)) ([baba888](https://www.github.com/googleapis/python-documentai/commit/baba888184d6cc872e048aefd52b14d2486c553f))
* add Samples section to CONTRIBUTING.rst ([#181](https://www.github.com/googleapis/python-documentai/issues/181)) ([b0f4c7a](https://www.github.com/googleapis/python-documentai/commit/b0f4c7ab32d7b864eade29e44efc1b51c80fb3e1))


## [0.5.0](https://www.github.com/googleapis/python-documentai/compare/v0.4.0...v0.5.0) (2021-05-28)


### Features

* add confidence field to the PageAnchor.PageRef in document.proto. ([be671a8](https://www.github.com/googleapis/python-documentai/commit/be671a832839d6efeae76d168b7913a9408572b4))
* support self-signed JWT flow for service accounts ([be671a8](https://www.github.com/googleapis/python-documentai/commit/be671a832839d6efeae76d168b7913a9408572b4))
* Use non-regionalized default host name for documentai.googleapis.com ([be671a8](https://www.github.com/googleapis/python-documentai/commit/be671a832839d6efeae76d168b7913a9408572b4))


### Bug Fixes

* add async client to %name_%version/init.py ([be671a8](https://www.github.com/googleapis/python-documentai/commit/be671a832839d6efeae76d168b7913a9408572b4))
* Parsing pages, but should be paragraphs ([#147](https://www.github.com/googleapis/python-documentai/issues/147)) ([c4aca1b](https://www.github.com/googleapis/python-documentai/commit/c4aca1bc1c01b3e1fdcc644eaf8922552c6c99a7))

## [0.4.0](https://www.github.com/googleapis/python-documentai/compare/v0.3.0...v0.4.0) (2021-03-25)


### Features

* add 'from_service_account_info' factory to clients ([d6f183a](https://www.github.com/googleapis/python-documentai/commit/d6f183a696b211c6d29bc28e9bbd0a8537f65577))
* add common resource path helpers, expose client transport ([#43](https://www.github.com/googleapis/python-documentai/issues/43)) ([4918e62](https://www.github.com/googleapis/python-documentai/commit/4918e62033b4c118bf99ba83730377b4ecc86d17))
* add documentai v1 ([#101](https://www.github.com/googleapis/python-documentai/issues/101)) ([74fabb5](https://www.github.com/googleapis/python-documentai/commit/74fabb5e260ecc27e9cf005502d79590fa7f72e4))
* add from_service_account_info factory and fix sphinx identifiers  ([#80](https://www.github.com/googleapis/python-documentai/issues/80)) ([d6f183a](https://www.github.com/googleapis/python-documentai/commit/d6f183a696b211c6d29bc28e9bbd0a8537f65577))


### Bug Fixes

* added if statement to filter out dir blob files ([#63](https://www.github.com/googleapis/python-documentai/issues/63)) ([7f7f541](https://www.github.com/googleapis/python-documentai/commit/7f7f541bcf4d2f42b2f619c2ceb45f53c5d0e9eb))
* adds comment with explicit hostname change ([#94](https://www.github.com/googleapis/python-documentai/issues/94)) ([bb639f9](https://www.github.com/googleapis/python-documentai/commit/bb639f9470304b9c408143a3e8091a4ca8c54160))
* fix sphinx identifiers ([d6f183a](https://www.github.com/googleapis/python-documentai/commit/d6f183a696b211c6d29bc28e9bbd0a8537f65577))
* moves import statment inside region tags ([#71](https://www.github.com/googleapis/python-documentai/issues/71)) ([a04fbea](https://www.github.com/googleapis/python-documentai/commit/a04fbeaf026d3d204dbb6c6cecf181068ddcc882))
* remove client recv msg limit and add enums to `types/__init__.py` ([#72](https://www.github.com/googleapis/python-documentai/issues/72)) ([c94afd5](https://www.github.com/googleapis/python-documentai/commit/c94afd55124b0abc8978bf86b84743dd4afb0778))
* removes C-style semicolons and slash comments ([#59](https://www.github.com/googleapis/python-documentai/issues/59)) ([1b24bfd](https://www.github.com/googleapis/python-documentai/commit/1b24bfdfc603952db8d1c633dfde108a396aa707))
* **samples:** swaps 'continue' for 'return' ([#93](https://www.github.com/googleapis/python-documentai/issues/93)) ([dabe48e](https://www.github.com/googleapis/python-documentai/commit/dabe48e8c1439ceb8a50c18aa3c7dca848a9117a))


### Documentation

* fix pypi link ([#46](https://www.github.com/googleapis/python-documentai/issues/46)) ([5162674](https://www.github.com/googleapis/python-documentai/commit/5162674091b9a2111b90eb26739b4e11f9119582))
* **samples:** new Doc AI samples for v1beta3 ([#44](https://www.github.com/googleapis/python-documentai/issues/44)) ([cc8c58d](https://www.github.com/googleapis/python-documentai/commit/cc8c58d1bade4be53fde08f6a3497eb3f79f63b1))

## [0.3.0](https://www.github.com/googleapis/python-documentai/compare/v0.2.0...v0.3.0) (2020-09-30)


### Features

* add async client ([#26](https://www.github.com/googleapis/python-documentai/issues/26)) ([ea83083](https://www.github.com/googleapis/python-documentai/commit/ea83083c315d4a97c29df35955f9547e2f869114))
* add v1beta3 ([#34](https://www.github.com/googleapis/python-documentai/issues/34)) ([6145da3](https://www.github.com/googleapis/python-documentai/commit/6145da3d5a5032f9df59ea2a499dccbf24809841))


### Bug Fixes

* **python:** change autodoc_default_flags to autodoc_default_options ([#27](https://www.github.com/googleapis/python-documentai/issues/27)) ([4eefc0a](https://www.github.com/googleapis/python-documentai/commit/4eefc0abf9a36cff8639c16c49d09487433b325b))

## [0.2.0](https://www.github.com/googleapis/python-documentai/compare/v0.1.0...v0.2.0) (2020-05-28)


### Features

* add mtls support ([#18](https://www.github.com/googleapis/python-documentai/issues/18)) ([50814b4](https://www.github.com/googleapis/python-documentai/commit/50814b448fba6c3f1da5e5ebf446bd91abff6811))

## 0.1.0 (2020-04-01)


### Features

* **documentai:** bump copyright year to 2020, tweak docstring formatting (via synth) [[#10230](https://www.github.com/googleapis/python-documentai/issues/10230)) ([329dbcf](https://www.github.com/googleapis/python-documentai/commit/329dbcfd8672cdea3a15779e7a2634f80d3d7753))
* **documentai:** initial generation of documentai ([#9623](https://www.github.com/googleapis/python-documentai/issues/9623)) ([fc3d29f](https://www.github.com/googleapis/python-documentai/commit/fc3d29fd388531b0e7d2812ceef4bc26a3cb1c7b))
* add v1beta2, remove v1beta1 ([#13](https://www.github.com/googleapis/python-documentai/issues/13)) ([1d8efd9](https://www.github.com/googleapis/python-documentai/commit/1d8efd9d74b8ae4c865751f60a01baed5a8d8d24))
