# Changelog

## 0.22.0 (2023-11-03)

Full Changelog: [v0.21.0...v0.22.0](https://github.com/lithic-com/lithic-python/compare/v0.21.0...v0.22.0)

### Features

* **api:** add verification_attempts response property ([#223](https://github.com/lithic-com/lithic-python/issues/223)) ([84446d7](https://github.com/lithic-com/lithic-python/commit/84446d7a9e69bfe2bc4b22dca2b15ba4cfd053d5))
* **client:** allow binary returns ([#224](https://github.com/lithic-com/lithic-python/issues/224)) ([78c7e86](https://github.com/lithic-com/lithic-python/commit/78c7e86a3930f9174e23363734499ff9b6fd1417))
* **client:** support accessing raw response objects ([#218](https://github.com/lithic-com/lithic-python/issues/218)) ([8540bba](https://github.com/lithic-com/lithic-python/commit/8540bbac962b5241d01aee47e518033e0dfa6c5e))
* **client:** support passing BaseModels to request params at runtime ([#225](https://github.com/lithic-com/lithic-python/issues/225)) ([ab37ce8](https://github.com/lithic-com/lithic-python/commit/ab37ce804c856b42f2964e5fc882a96199b2554d))
* **github:** include a devcontainer setup ([#222](https://github.com/lithic-com/lithic-python/issues/222)) ([1256ea0](https://github.com/lithic-com/lithic-python/commit/1256ea00c91a566685741806c0611f32fa74a89c))
* **package:** add classifiers ([#221](https://github.com/lithic-com/lithic-python/issues/221)) ([a1d9641](https://github.com/lithic-com/lithic-python/commit/a1d9641c633db15dff8306d45a555dcbb561a75a))


### Chores

* **internal:** minor restructuring of base client ([#220](https://github.com/lithic-com/lithic-python/issues/220)) ([2c36aa7](https://github.com/lithic-com/lithic-python/commit/2c36aa7f52575c37a7152bdfa00bc2fa5c37de92))
* **internal:** require explicit overrides ([#217](https://github.com/lithic-com/lithic-python/issues/217)) ([c85bd62](https://github.com/lithic-com/lithic-python/commit/c85bd6213a6d8a3bbceccc700ed9004ce4d3f0cd))

## 0.21.0 (2023-10-26)

Full Changelog: [v0.20.0...v0.21.0](https://github.com/lithic-com/lithic-python/compare/v0.20.0...v0.21.0)

### Features

* **api:** add CardProgram and DigitalCardArt resources ([#213](https://github.com/lithic-com/lithic-python/issues/213)) ([afcb7e4](https://github.com/lithic-com/lithic-python/commit/afcb7e416ee7ced7e67e5c0fd3374f13fee7b2f0))

## 0.20.0 (2023-10-25)

Full Changelog: [v0.19.3...v0.20.0](https://github.com/lithic-com/lithic-python/compare/v0.19.3...v0.20.0)

### Features

* **api:** add AUTH_STREAM_ACCESS to responder endpoints ([#205](https://github.com/lithic-com/lithic-python/issues/205)) ([55d9f21](https://github.com/lithic-com/lithic-python/commit/55d9f2157baa536a789242c175f02049ac375eb0))
* **api:** add verification_failed_reason ([#203](https://github.com/lithic-com/lithic-python/issues/203)) ([b6dfb4d](https://github.com/lithic-com/lithic-python/commit/b6dfb4d6942029db5d7f7be801c50c3a68bbf0de))
* **api:** updates ([#197](https://github.com/lithic-com/lithic-python/issues/197)) ([34f3534](https://github.com/lithic-com/lithic-python/commit/34f3534570052d2aac66fb377fff2f0070e3bba1))
* **client:** add logging setup ([#187](https://github.com/lithic-com/lithic-python/issues/187)) ([4ec658e](https://github.com/lithic-com/lithic-python/commit/4ec658e9ab1198fee4c7c56565e373544c8f0dc2))
* **client:** adjust retry behavior to be exponential backoff ([#209](https://github.com/lithic-com/lithic-python/issues/209)) ([b571389](https://github.com/lithic-com/lithic-python/commit/b57138988410db4d48aaec60c6a9e89a77417d93))
* **client:** improve file upload types ([#208](https://github.com/lithic-com/lithic-python/issues/208)) ([ff0cca0](https://github.com/lithic-com/lithic-python/commit/ff0cca01295b23feca0afd7acf2d4850c711b1c8))
* **client:** support passing httpx.URL instances to base_url ([#199](https://github.com/lithic-com/lithic-python/issues/199)) ([fec5362](https://github.com/lithic-com/lithic-python/commit/fec5362238f361bc02574eadda2b851331303922))
* make webhook headers case insensitive ([#190](https://github.com/lithic-com/lithic-python/issues/190)) ([e0a5811](https://github.com/lithic-com/lithic-python/commit/e0a58115203e16b042a27ccae640e49bfabc4bfe))


### Bug Fixes

* **client:** accept io.IOBase instances in file params ([#194](https://github.com/lithic-com/lithic-python/issues/194)) ([c41ebb0](https://github.com/lithic-com/lithic-python/commit/c41ebb0bc989ec82dc443e328078dbbbebc7882b))
* **client:** correctly handle arguments with env vars ([#188](https://github.com/lithic-com/lithic-python/issues/188)) ([1bc8b58](https://github.com/lithic-com/lithic-python/commit/1bc8b58c1ff0669047ca2d62fa990ea2f4f3a33c))


### Chores

* **docs:** remove old migration guide ([#212](https://github.com/lithic-com/lithic-python/issues/212)) ([ee6cbb4](https://github.com/lithic-com/lithic-python/commit/ee6cbb4c0e34ab632bc15c0ab1604edd85595536))
* **internal:** bump mypy ([#207](https://github.com/lithic-com/lithic-python/issues/207)) ([74308ad](https://github.com/lithic-com/lithic-python/commit/74308ad963fbd4b4591eb3f2a0ecc9b3dafdabf9))
* **internal:** bump pyright ([#206](https://github.com/lithic-com/lithic-python/issues/206)) ([d65667f](https://github.com/lithic-com/lithic-python/commit/d65667fbf6484c9bab412b66fb7cac5373b0d70b))
* **internal:** cleanup some redundant code ([#193](https://github.com/lithic-com/lithic-python/issues/193)) ([61a777a](https://github.com/lithic-com/lithic-python/commit/61a777ad39c3c41e9f834583a6de7108d7878570))
* **internal:** enable lint rule ([#192](https://github.com/lithic-com/lithic-python/issues/192)) ([df95673](https://github.com/lithic-com/lithic-python/commit/df956735de9c13c50be6406d9b1ea539dd6bb656))
* **internal:** improve publish script ([#198](https://github.com/lithic-com/lithic-python/issues/198)) ([9ecaa3c](https://github.com/lithic-com/lithic-python/commit/9ecaa3c95313fe60d79dda3ff8309e1652bbda52))
* **internal:** migrate from Poetry to Rye ([#196](https://github.com/lithic-com/lithic-python/issues/196)) ([748a670](https://github.com/lithic-com/lithic-python/commit/748a6709bdd0207cd35faf4b4d768d5676b2da18))
* **internal:** update gitignore ([#201](https://github.com/lithic-com/lithic-python/issues/201)) ([631d650](https://github.com/lithic-com/lithic-python/commit/631d6502ccc147ba606099572dc8671faf2be1f1))
* **internal:** update gitignore ([#202](https://github.com/lithic-com/lithic-python/issues/202)) ([48a9f60](https://github.com/lithic-com/lithic-python/commit/48a9f6013454853fcb9162d1860f0d5ad31def42))
* **internal:** update lock file ([#200](https://github.com/lithic-com/lithic-python/issues/200)) ([19aad77](https://github.com/lithic-com/lithic-python/commit/19aad77f824a3c454cbd3c03ed82996c387e896f))
* update comment ([#191](https://github.com/lithic-com/lithic-python/issues/191)) ([c5e2a68](https://github.com/lithic-com/lithic-python/commit/c5e2a687b9a0ea0960046b00fa30b7cd46f7f730))
* update README ([#184](https://github.com/lithic-com/lithic-python/issues/184)) ([bda1154](https://github.com/lithic-com/lithic-python/commit/bda11547b33249121ef97a221e9e7d7f851aa490))


### Documentation

* improve to dictionary example ([#211](https://github.com/lithic-com/lithic-python/issues/211)) ([773b0f5](https://github.com/lithic-com/lithic-python/commit/773b0f59bf5b65a99f0e707e5bda028ff7632b98))
* organisation -&gt; organization (UK to US English) ([#195](https://github.com/lithic-com/lithic-python/issues/195)) ([d082979](https://github.com/lithic-com/lithic-python/commit/d08297944533fb314f4e5c38501be4bfa58c9e54))


### Refactors

* **test:** refactor authentication tests ([#186](https://github.com/lithic-com/lithic-python/issues/186)) ([2357bdd](https://github.com/lithic-com/lithic-python/commit/2357bdddb8a2f5f352c797fdc3e470ad4146c44b))

## 0.19.3 (2023-10-11)

Full Changelog: [v0.19.2...v0.19.3](https://github.com/lithic-com/lithic-python/compare/v0.19.2...v0.19.3)

### Features

* **client:** add forwards-compatible pydantic methods ([#181](https://github.com/lithic-com/lithic-python/issues/181)) ([0bb14e3](https://github.com/lithic-com/lithic-python/commit/0bb14e3c29d81a59942cf4a2d4c07cf056228afc))
* **client:** add support for passing in a httpx client ([#183](https://github.com/lithic-com/lithic-python/issues/183)) ([c2a69fb](https://github.com/lithic-com/lithic-python/commit/c2a69fbbf70b4755e7aa23dca5cf9ca8c1208631))

## 0.19.2 (2023-10-05)

Full Changelog: [v0.19.1...v0.19.2](https://github.com/lithic-com/lithic-python/compare/v0.19.1...v0.19.2)

### Features

* **api:** updates ([#179](https://github.com/lithic-com/lithic-python/issues/179)) ([c51c060](https://github.com/lithic-com/lithic-python/commit/c51c06045efd887584b31f212bac7f4b7dea88d8))

## 0.19.1 (2023-10-03)

Full Changelog: [v0.19.0...v0.19.1](https://github.com/lithic-com/lithic-python/compare/v0.19.0...v0.19.1)

### Features

* **client:** handle retry-after header with a date format ([#176](https://github.com/lithic-com/lithic-python/issues/176)) ([3d6fbc8](https://github.com/lithic-com/lithic-python/commit/3d6fbc8de998bf1f5694bddf2e533b0ec5decdbd))


### Chores

* **ci:** remove reviewer ([#175](https://github.com/lithic-com/lithic-python/issues/175)) ([b9778de](https://github.com/lithic-com/lithic-python/commit/b9778de4087a8d41680cc36c82606a03ba508814))
* **tests:** update test examples ([#178](https://github.com/lithic-com/lithic-python/issues/178)) ([4f4d48e](https://github.com/lithic-com/lithic-python/commit/4f4d48e41d25a6d0ff47121405430ccdf4e8b5ce))

## 0.19.0 (2023-09-29)

Full Changelog: [v0.18.6...v0.19.0](https://github.com/lithic-com/lithic-python/compare/v0.18.6...v0.19.0)

### ⚠ BREAKING CHANGES

* **api:** remove `post /webhooks/account_holders` endpoint ([#171](https://github.com/lithic-com/lithic-python/issues/171))

### Refactors

* **api:** remove `post /webhooks/account_holders` endpoint ([#171](https://github.com/lithic-com/lithic-python/issues/171)) ([a2143d4](https://github.com/lithic-com/lithic-python/commit/a2143d494256fdb142122a54af556d0f3a8bfce7))

## 0.18.6 (2023-09-27)

Full Changelog: [v0.18.5...v0.18.6](https://github.com/lithic-com/lithic-python/compare/v0.18.5...v0.18.6)

### Features

* **package:** export a root error type ([#169](https://github.com/lithic-com/lithic-python/issues/169)) ([f4e57de](https://github.com/lithic-com/lithic-python/commit/f4e57decb9debf8e31e55fcd6ce1204656858228))


### Bug Fixes

* **client:** don't error by default for unexpected content types ([#166](https://github.com/lithic-com/lithic-python/issues/166)) ([cf9c611](https://github.com/lithic-com/lithic-python/commit/cf9c611ba78ac4e0ada060e9ecda7a387caba251))


### Chores

* **internal:** move error classes from _base_exceptions to _exceptions (⚠️ breaking) ([#168](https://github.com/lithic-com/lithic-python/issues/168)) ([f959dd5](https://github.com/lithic-com/lithic-python/commit/f959dd56cd0692c80ffb165eff2e965a5bc4ccf3))
* **tests:** improve raw response test ([#170](https://github.com/lithic-com/lithic-python/issues/170)) ([0848bd0](https://github.com/lithic-com/lithic-python/commit/0848bd0663d0424ddba2826ab207c46ea266cf50))

## 0.18.5 (2023-09-20)

Full Changelog: [v0.18.4...v0.18.5](https://github.com/lithic-com/lithic-python/compare/v0.18.4...v0.18.5)

### Features

* **api:** add simulation endpoints, event types, fix transfer request AuthRule ([#164](https://github.com/lithic-com/lithic-python/issues/164)) ([ca1e3dc](https://github.com/lithic-com/lithic-python/commit/ca1e3dc32ef7faece3c3502ae0083a8f28b42fd3))

## 0.18.4 (2023-09-15)

Full Changelog: [v0.18.3...v0.18.4](https://github.com/lithic-com/lithic-python/compare/v0.18.3...v0.18.4)

### Features

* **client:** retry on 408 Request Timeout ([#160](https://github.com/lithic-com/lithic-python/issues/160)) ([9ef57a3](https://github.com/lithic-com/lithic-python/commit/9ef57a3a53884a3a587d426f57bc1c3646fb610a))


### Bug Fixes

* **client:** properly configure model set fields ([#159](https://github.com/lithic-com/lithic-python/issues/159)) ([1c13556](https://github.com/lithic-com/lithic-python/commit/1c135563927c96796ce287184ab7de0c4ff0d150))


### Chores

* **internal:** add helpers ([#161](https://github.com/lithic-com/lithic-python/issues/161)) ([cbfebd7](https://github.com/lithic-com/lithic-python/commit/cbfebd70a47f4434f3386b69b375ca10389f2466))


### Documentation

* add some missing inline documentation ([#156](https://github.com/lithic-com/lithic-python/issues/156)) ([e1a3ac0](https://github.com/lithic-com/lithic-python/commit/e1a3ac05d29d792e1b3947e048bea43b03d2e7cd))

## 0.18.3 (2023-09-11)

Full Changelog: [v0.18.2...v0.18.3](https://github.com/lithic-com/lithic-python/compare/v0.18.2...v0.18.3)

### Features

* **api:** add Simulate Return Payment endpoint ([#155](https://github.com/lithic-com/lithic-python/issues/155)) ([b81d2ac](https://github.com/lithic-com/lithic-python/commit/b81d2aca3079b553f064159c74f4ba25178cf97e))
* **api:** add tokenizations.simulate and correct typo'd enum  ([#151](https://github.com/lithic-com/lithic-python/issues/151)) ([8968036](https://github.com/lithic-com/lithic-python/commit/896803650b1bf00753f17f31053cde068f35a4d2))
* **api:** add user defined id ([#144](https://github.com/lithic-com/lithic-python/issues/144)) ([88a2f52](https://github.com/lithic-com/lithic-python/commit/88a2f52a45f26c342148cf29d1c5883b0ba79b12))
* fixes tests where an array has to have unique enum values ([#147](https://github.com/lithic-com/lithic-python/issues/147)) ([0dbc2e6](https://github.com/lithic-com/lithic-python/commit/0dbc2e664471d2889cdd40e584591e1b8e155e7c))
* **types:** remove unused types ([#145](https://github.com/lithic-com/lithic-python/issues/145)) ([9e13e49](https://github.com/lithic-com/lithic-python/commit/9e13e4936d31f789b38853a9a9930398bf989527))


### Bug Fixes

* **client:** properly handle optional file params ([#146](https://github.com/lithic-com/lithic-python/issues/146)) ([15a0f07](https://github.com/lithic-com/lithic-python/commit/15a0f07400b61f1d99fae443226ac9dbeac8b1a3))


### Chores

* **ci:** setup workflows to create releases and release PRs ([#137](https://github.com/lithic-com/lithic-python/issues/137)) ([9d5ba39](https://github.com/lithic-com/lithic-python/commit/9d5ba39e3f2ff9fbf9956629b54c6511711bd6a4))
* **internal:** add `pydantic.generics` import for compatibility ([#139](https://github.com/lithic-com/lithic-python/issues/139)) ([1933c6d](https://github.com/lithic-com/lithic-python/commit/1933c6d7e08bb8b0c0642dcfcd0c7cf796f10362))
* **internal:** cleanup test params ([#152](https://github.com/lithic-com/lithic-python/issues/152)) ([99e8a4b](https://github.com/lithic-com/lithic-python/commit/99e8a4b9b7e2d9b2b71877e879776e4c970830d1))
* **internal:** minor restructuring ([#142](https://github.com/lithic-com/lithic-python/issues/142)) ([65f9fc7](https://github.com/lithic-com/lithic-python/commit/65f9fc72aeb22556fb1beea1ea796bd7eac99c9c))
* **internal:** minor update ([#149](https://github.com/lithic-com/lithic-python/issues/149)) ([b65dcfa](https://github.com/lithic-com/lithic-python/commit/b65dcfa341221f1f2727f667ac009642205245f4))
* **internal:** update base client ([#148](https://github.com/lithic-com/lithic-python/issues/148)) ([7596e42](https://github.com/lithic-com/lithic-python/commit/7596e427559f2e271b1d6290960872510c70fcbd))
* **internal:** update pyright ([#154](https://github.com/lithic-com/lithic-python/issues/154)) ([d44c079](https://github.com/lithic-com/lithic-python/commit/d44c079d71f827a22a43a90e89b61f71fa94c06b))
* **internal:** updates ([#153](https://github.com/lithic-com/lithic-python/issues/153)) ([6d674bc](https://github.com/lithic-com/lithic-python/commit/6d674bcb807005692c71451f5ebf5844f6761edf))


### Documentation

* **readme:** add link to api.md ([#150](https://github.com/lithic-com/lithic-python/issues/150)) ([bb82d1d](https://github.com/lithic-com/lithic-python/commit/bb82d1dd49c81672be1bcd3fbd7582e400d511b2))
* **readme:** reference pydantic helpers ([#143](https://github.com/lithic-com/lithic-python/issues/143)) ([f0d51be](https://github.com/lithic-com/lithic-python/commit/f0d51bee688b94115132af05caf32a68a8b11002))

## [0.18.2](https://github.com/lithic-com/lithic-python/compare/v0.18.1...v0.18.2) (2023-08-24)


### Chores

* **internal:** bump pydantic dep ([#132](https://github.com/lithic-com/lithic-python/issues/132)) ([cb59327](https://github.com/lithic-com/lithic-python/commit/cb59327cec4a5e3fcf956fba0c14422680b0657e))
* **internal:** update anyio ([#134](https://github.com/lithic-com/lithic-python/issues/134)) ([2acb7f6](https://github.com/lithic-com/lithic-python/commit/2acb7f69ed9b580122000c1f83d1d5ba895bfae2))

## [0.18.1](https://github.com/lithic-com/lithic-python/compare/v0.18.0...v0.18.1) (2023-08-17)


### Features

* add support for Pydantic v2 ([#129](https://github.com/lithic-com/lithic-python/issues/129)) ([1f44714](https://github.com/lithic-com/lithic-python/commit/1f4471429a7cc391678e889eef74127658f5f90c))

## [0.18.0](https://github.com/lithic-com/lithic-python/compare/v0.17.8...v0.18.0) (2023-08-15)


### ⚠ BREAKING CHANGES

* **api:** change `key` to `secret` ([#121](https://github.com/lithic-com/lithic-python/issues/121))

### Features

* allow a default timeout to be set for clients ([#123](https://github.com/lithic-com/lithic-python/issues/123)) ([13ce2e8](https://github.com/lithic-com/lithic-python/commit/13ce2e8aa1bdde7eab870adb360d808e203ff3eb))
* **api:** change `key` to `secret` ([#121](https://github.com/lithic-com/lithic-python/issues/121)) ([faec3a2](https://github.com/lithic-com/lithic-python/commit/faec3a2442cf6c4937be5574405b5e81d4e618d1))


### Styles

* prefer importing types directly instead of module names ([#124](https://github.com/lithic-com/lithic-python/issues/124)) ([5048bec](https://github.com/lithic-com/lithic-python/commit/5048becd3e1606baf1511c39baf8d1bc5a2027b7))


### Chores

* assign default reviewers to release PRs ([#125](https://github.com/lithic-com/lithic-python/issues/125)) ([0ace592](https://github.com/lithic-com/lithic-python/commit/0ace59209c593e698d8c6ef49d6edc04939614e8))
* **client:** send Idempotency-Key header ([#127](https://github.com/lithic-com/lithic-python/issues/127)) ([f387e15](https://github.com/lithic-com/lithic-python/commit/f387e15ec7517a4ac802cf3e71526660eb98ebec))
* **internal:** minor formatting change ([#126](https://github.com/lithic-com/lithic-python/issues/126)) ([0093e61](https://github.com/lithic-com/lithic-python/commit/0093e6167b942e23ce6c74621274bcd198ba731e))

## [0.17.8](https://github.com/lithic-com/lithic-python/compare/v0.17.7...v0.17.8) (2023-08-11)


### Features

* allOf models now have toXxx methods to access the separate allOf models ([#117](https://github.com/lithic-com/lithic-python/issues/117)) ([f6103e9](https://github.com/lithic-com/lithic-python/commit/f6103e95f563dc53bdf9f97d1ddf755277008afa))
* **api:** add card reissue shipping options ([#116](https://github.com/lithic-com/lithic-python/issues/116)) ([ed1bad9](https://github.com/lithic-com/lithic-python/commit/ed1bad98fdf5e6847e95d4fb71006930d22bc580))


### Chores

* **deps:** bump typing-extensions to 4.5 ([#118](https://github.com/lithic-com/lithic-python/issues/118)) ([0fc438c](https://github.com/lithic-com/lithic-python/commit/0fc438c952984ce9e2c41623518607c65f9bc11f))
* **internal/deps:** update lock file ([#115](https://github.com/lithic-com/lithic-python/issues/115)) ([fa87728](https://github.com/lithic-com/lithic-python/commit/fa87728a052dd9184e10db98e834926bb72075b8))
* **internal:** bump pytest-asyncio ([#119](https://github.com/lithic-com/lithic-python/issues/119)) ([5e041e1](https://github.com/lithic-com/lithic-python/commit/5e041e1b8bebdf1ae2606b90f6056614505b6105))
* **internal:** minor import restructuring ([#113](https://github.com/lithic-com/lithic-python/issues/113)) ([47e1b9f](https://github.com/lithic-com/lithic-python/commit/47e1b9fc29504c987faac62bd853bad7b6d36197))

## [0.17.7](https://github.com/lithic-com/lithic-python/compare/v0.17.6...v0.17.7) (2023-08-08)


### Features

* **api:** add carrier property to card create and reissue params ([#111](https://github.com/lithic-com/lithic-python/issues/111)) ([a2d0279](https://github.com/lithic-com/lithic-python/commit/a2d027970a3685bcf0269e0de3a0218d88ef03c6))


### Documentation

* **readme:** remove beta status + document versioning policy ([#108](https://github.com/lithic-com/lithic-python/issues/108)) ([b7dc50d](https://github.com/lithic-com/lithic-python/commit/b7dc50dfe8dd2f6fe93d9a3a77d40f595846c8c7))


### Chores

* **internal:** bump certifi dependency ([#110](https://github.com/lithic-com/lithic-python/issues/110)) ([8994910](https://github.com/lithic-com/lithic-python/commit/899491010dbee90dc2374361bc5a38c5b33b3d3f))
* **internal:** bump lock file ([#107](https://github.com/lithic-com/lithic-python/issues/107)) ([123fad1](https://github.com/lithic-com/lithic-python/commit/123fad1eca60bb9798af74c82ecc03678e6282f6))
* **internal:** update mypy to v1.4.1 ([#105](https://github.com/lithic-com/lithic-python/issues/105)) ([22bac04](https://github.com/lithic-com/lithic-python/commit/22bac04159d2457ff29a7de8ba303ab68f05c9db))
* **internal:** update ruff to v0.0.282 ([#109](https://github.com/lithic-com/lithic-python/issues/109)) ([fb5124a](https://github.com/lithic-com/lithic-python/commit/fb5124acdda2188c66a27334932c78ee9e405e68))

## [0.17.6](https://github.com/lithic-com/lithic-python/compare/v0.17.5...v0.17.6) (2023-08-01)


### Features

* **api:** updates ([#102](https://github.com/lithic-com/lithic-python/issues/102)) ([98b247e](https://github.com/lithic-com/lithic-python/commit/98b247e54a15fc1e725481bdb6ca651a33ae7658))
* **client:** add client close handlers ([#97](https://github.com/lithic-com/lithic-python/issues/97)) ([34560c3](https://github.com/lithic-com/lithic-python/commit/34560c372ba69b2bfc8f4b72013544961a410a40))


### Bug Fixes

* adjust typo of 'descisioning' to 'decisioning' ([#103](https://github.com/lithic-com/lithic-python/issues/103)) ([2b0c0e7](https://github.com/lithic-com/lithic-python/commit/2b0c0e7f03e19a60582d03ea9f40c862493dfd88))
* **client:** correctly handle environment variable access ([#95](https://github.com/lithic-com/lithic-python/issues/95)) ([1666080](https://github.com/lithic-com/lithic-python/commit/166608080f2245af170c11a9f5a10ce3bbe1ded6))


### Chores

* **internal:** bump pyright ([#100](https://github.com/lithic-com/lithic-python/issues/100)) ([096cf19](https://github.com/lithic-com/lithic-python/commit/096cf193324ac422682a6965b7c00ba69885d11d))
* **internal:** bump pyright ([#101](https://github.com/lithic-com/lithic-python/issues/101)) ([cfa2725](https://github.com/lithic-com/lithic-python/commit/cfa2725b4d28acb78aa3595383281407b2de4fcb))
* **internal:** make demo example runnable and more portable ([#99](https://github.com/lithic-com/lithic-python/issues/99)) ([538860c](https://github.com/lithic-com/lithic-python/commit/538860c859a309ed60709cf5f41cb8653252a349))
* **internal:** minor reformatting of code ([#98](https://github.com/lithic-com/lithic-python/issues/98)) ([c6c7133](https://github.com/lithic-com/lithic-python/commit/c6c7133ea915c441b53169bf622415a37f403cbc))

## [0.17.5](https://github.com/lithic-com/lithic-python/compare/v0.17.4...v0.17.5) (2023-07-27)


### Features

* **api:** add payment and external bank accounts resource ([#91](https://github.com/lithic-com/lithic-python/issues/91)) ([9a63218](https://github.com/lithic-com/lithic-python/commit/9a63218bce1a24624748e49673fb19efcf12b2cc))


### Documentation

* **readme:** use `client` everywhere for consistency ([#93](https://github.com/lithic-com/lithic-python/issues/93)) ([be4350d](https://github.com/lithic-com/lithic-python/commit/be4350df71c7b05fdb394098e0ef326917571be7))

## [0.17.4](https://github.com/lithic-com/lithic-python/compare/v0.17.3...v0.17.4) (2023-07-21)


### Features

* **api:** add `with_content` param ([#87](https://github.com/lithic-com/lithic-python/issues/87)) ([a8f6ca8](https://github.com/lithic-com/lithic-python/commit/a8f6ca80c7657e143451bd6ba97e156a6b1f346f))


### Documentation

* **readme:** reference "client" in errors section and add missing import ([#89](https://github.com/lithic-com/lithic-python/issues/89)) ([66127cc](https://github.com/lithic-com/lithic-python/commit/66127cc6aa93d707e26bf2b9bb4e090b4c473563))

## [0.17.3](https://github.com/lithic-com/lithic-python/compare/v0.17.2...v0.17.3) (2023-07-18)


### Features

* **api:** add event message attempts ([#84](https://github.com/lithic-com/lithic-python/issues/84)) ([c3c9942](https://github.com/lithic-com/lithic-python/commit/c3c9942b104b3c0e3346b1b52c98ae172462f244))

## [0.17.2](https://github.com/lithic-com/lithic-python/compare/v0.17.1...v0.17.2) (2023-07-17)


### Features

* **api:** add more enum members to event types ([#79](https://github.com/lithic-com/lithic-python/issues/79)) ([3e57d94](https://github.com/lithic-com/lithic-python/commit/3e57d94cc1f0079474fd7d4c9b75dde93d6a72b3))
* **api:** no longer require `website_url` property on KYB object ([#82](https://github.com/lithic-com/lithic-python/issues/82)) ([673a1c3](https://github.com/lithic-com/lithic-python/commit/673a1c3866611db00849967e88918238d3435235))


### Chores

* **internal:** add `codegen.log` to `.gitignore` ([#81](https://github.com/lithic-com/lithic-python/issues/81)) ([ec2ea75](https://github.com/lithic-com/lithic-python/commit/ec2ea75d55edbf9de9df2babedbfcef2e8baad0a))

## [0.17.1](https://github.com/lithic-com/lithic-python/compare/v0.17.0...v0.17.1) (2023-07-12)


### Features

* **api:** add `state` query param for cards ([#73](https://github.com/lithic-com/lithic-python/issues/73)) ([84fc0f5](https://github.com/lithic-com/lithic-python/commit/84fc0f53fa1a25c72bff1bf44ac910a8f84797c2))
* **api:** add digital wallet tokenization result event type ([#74](https://github.com/lithic-com/lithic-python/issues/74)) ([e3e21be](https://github.com/lithic-com/lithic-python/commit/e3e21be87c40a48731a109a4a2cc8031b0e22432))


### Bug Fixes

* **client:** use correct units for account holders create timeout ([#75](https://github.com/lithic-com/lithic-python/issues/75)) ([54915d3](https://github.com/lithic-com/lithic-python/commit/54915d32580689529831b91dfd6f2026e85634ee))


### Chores

* **package:** pin major versions of dependencies ([#76](https://github.com/lithic-com/lithic-python/issues/76)) ([9fd090c](https://github.com/lithic-com/lithic-python/commit/9fd090c22a4ee685794e52a5d7ef78536861b579))
* **package:** pin major versions of dependencies ([#77](https://github.com/lithic-com/lithic-python/issues/77)) ([0635c8b](https://github.com/lithic-com/lithic-python/commit/0635c8bd33a9f88e938323e640c262452025ae2a))

## [0.17.0](https://github.com/lithic-com/lithic-python/compare/v0.16.2...v0.17.0) (2023-07-05)


### ⚠ BREAKING CHANGES

* **api:** remove previous_auth_rule_tokens from auth rules ([#69](https://github.com/lithic-com/lithic-python/issues/69))

### Chores

* **internal:** update lockfile ([#67](https://github.com/lithic-com/lithic-python/issues/67)) ([6b99cf3](https://github.com/lithic-com/lithic-python/commit/6b99cf3d08e15bbab1eb256e15f6acac39ef00a9))


### Refactors

* **api:** remove previous_auth_rule_tokens from auth rules ([#69](https://github.com/lithic-com/lithic-python/issues/69)) ([a6a3bc5](https://github.com/lithic-com/lithic-python/commit/a6a3bc5b2026875ea18e1b5b3d97cc2b13a8ada0))

## [0.16.2](https://github.com/lithic-com/lithic-python/compare/v0.16.1...v0.16.2) (2023-07-01)


### Bug Fixes

* **deps:** pin pydantic to less than v2.0 ([#65](https://github.com/lithic-com/lithic-python/issues/65)) ([57ec609](https://github.com/lithic-com/lithic-python/commit/57ec609c3f7d644db0c05d9847984384db08f711))


### Chores

* **deps:** update certifi ([#59](https://github.com/lithic-com/lithic-python/issues/59)) ([fecd16d](https://github.com/lithic-com/lithic-python/commit/fecd16d9a519c25649e52912d83d65303ada360a))
* **internal:** minor changes to code format ([#58](https://github.com/lithic-com/lithic-python/issues/58)) ([94f4518](https://github.com/lithic-com/lithic-python/commit/94f45184c0eb53908fb3bdc42efc363b450f1f1a))


### Styles

* minor reordering of types and properties ([#61](https://github.com/lithic-com/lithic-python/issues/61)) ([36fd9f0](https://github.com/lithic-com/lithic-python/commit/36fd9f0a5fbeb097141548ba33b3dc614ec34227))


### Documentation

* add trailing newlines ([#60](https://github.com/lithic-com/lithic-python/issues/60)) ([17deafc](https://github.com/lithic-com/lithic-python/commit/17deafc53de12af1009ac8e943b3e977a0606356))
* **api.md:** minor restructuring ([#63](https://github.com/lithic-com/lithic-python/issues/63)) ([2455100](https://github.com/lithic-com/lithic-python/commit/245510061002b63d05bf6ce0dba07010591d54ad))
* **api:** update account limits docstrings ([#55](https://github.com/lithic-com/lithic-python/issues/55)) ([0ea7cb1](https://github.com/lithic-com/lithic-python/commit/0ea7cb1485df5e3385bc4963c8b1824028a147ac))
* **api:** update limits docstrings ([#57](https://github.com/lithic-com/lithic-python/issues/57)) ([ab18e74](https://github.com/lithic-com/lithic-python/commit/ab18e74dd82747c309a7c9808fd1faf2a7e3c28c))

## [0.16.1](https://github.com/lithic-com/lithic-python/compare/v0.16.0...v0.16.1) (2023-06-19)


### Documentation

* **api:** clarify dispute evidence filename docstring ([#52](https://github.com/lithic-com/lithic-python/issues/52)) ([4116977](https://github.com/lithic-com/lithic-python/commit/4116977370e7c7df8a520cdc8e6bdc5bfe88ddda))

## [0.16.0](https://github.com/lithic-com/lithic-python/compare/v0.15.1...v0.16.0) (2023-06-15)


### ⚠ BREAKING CHANGES

* **api:** remove avs_type property, add dispute evidence filename, and mark properties nullable ([#51](https://github.com/lithic-com/lithic-python/issues/51))

### Features

* **api:** remove avs_type property, add dispute evidence filename, and mark properties nullable ([#51](https://github.com/lithic-com/lithic-python/issues/51)) ([0cce574](https://github.com/lithic-com/lithic-python/commit/0cce5748f8614aa9757c353e5b34c0ea1dab6945))


### Documentation

* point to github repo instead of email contact ([#47](https://github.com/lithic-com/lithic-python/issues/47)) ([90583fe](https://github.com/lithic-com/lithic-python/commit/90583fefac269e8b827fa98ef0ba8d2873ab4cf5))


### Chores

* **internal:** add overloads to `client.get` for streaming ([#49](https://github.com/lithic-com/lithic-python/issues/49)) ([7952321](https://github.com/lithic-com/lithic-python/commit/7952321cc5b8d3cd591f3d10e2e825b5ecb5c101))

## [0.15.1](https://github.com/lithic-com/lithic-python/compare/v0.15.0...v0.15.1) (2023-06-12)


### Bug Fixes

* properly handle key aliases in transform step ([#33](https://github.com/lithic-com/lithic-python/issues/33)) ([a4693bf](https://github.com/lithic-com/lithic-python/commit/a4693bfa14829276fb6b7a80ed4943b4529711b2))

## [0.15.0](https://github.com/lithic-com/lithic-python/compare/v0.14.4...v0.15.0) (2023-05-12)


### ⚠ BREAKING CHANGES

* **api:** replace `transaction_token` param in favour of `transaction_tokens` ([#28](https://github.com/lithic-com/lithic-python/issues/28))

### Refactors

* **api:** replace `transaction_token` param in favour of `transaction_tokens` ([#28](https://github.com/lithic-com/lithic-python/issues/28)) ([d1e7591](https://github.com/lithic-com/lithic-python/commit/d1e75916860def47fa61f9465cc8f2cfd33b7c10))

## [0.14.4](https://github.com/lithic-com/lithic-python/compare/v0.14.3...v0.14.4) (2023-05-12)


### Refactors

* change `event_types[]` param ([#23](https://github.com/lithic-com/lithic-python/issues/23)) ([a8c132c](https://github.com/lithic-com/lithic-python/commit/a8c132c74de6237a2424e613a85f2f1f08e499a1))

## [0.14.3](https://github.com/lithic-com/lithic-python/compare/v0.14.2...v0.14.3) (2023-05-11)


### Features

* **api:** add support for new `transaction_tokens` query param ([#19](https://github.com/lithic-com/lithic-python/issues/19)) ([20ce43e](https://github.com/lithic-com/lithic-python/commit/20ce43e20c4c7ee975894b4503232e030e7a33fd))
* **api:** updates ([#17](https://github.com/lithic-com/lithic-python/issues/17)) ([4365e71](https://github.com/lithic-com/lithic-python/commit/4365e719bab45b4d0d40d60bc1154b3b06f4555c))


### Bug Fixes

* **client:** correctly send array query params ([#21](https://github.com/lithic-com/lithic-python/issues/21)) ([cb95cb4](https://github.com/lithic-com/lithic-python/commit/cb95cb42478e4290b3d6a3f16211ac5024421459))

## [0.14.2](https://github.com/lithic-com/lithic-python/compare/v0.14.1...v0.14.2) (2023-05-05)


### Bug Fixes

* **event &gt; payload** type is now any object instead of unknown ([#8](https://github.com/lithic-com/lithic-python/issues/8)) ([a7830f7](https://github.com/lithic-com/lithic-python/commit/a7830f77157b5d0f3e82d1db3ffe1970206e3dc0))
* **pagination:** correct check for next page for cursor pagination ([#13](https://github.com/lithic-com/lithic-python/issues/13)) ([8070e51](https://github.com/lithic-com/lithic-python/commit/8070e5155e6ec0728d428a557db7202460964883))

## [0.14.1](https://github.com/lithic-com/lithic-python/compare/v0.14.0...v0.14.1) (2023-04-28)


### Features

* **api:** more detailed `post /disputes/{dispute_token}/evidences` response ([#5](https://github.com/lithic-com/lithic-python/issues/5)) ([1d9aba0](https://github.com/lithic-com/lithic-python/commit/1d9aba034dce04f743aa8860f1130306df261fd1))
