# Changelog

## 0.86.2 (2025-03-17)

Full Changelog: [v0.86.1...v0.86.2](https://github.com/lithic-com/lithic-python/compare/v0.86.1...v0.86.2)

### Bug Fixes

* **ci:** ensure pip is always available ([#714](https://github.com/lithic-com/lithic-python/issues/714)) ([9e8255b](https://github.com/lithic-com/lithic-python/commit/9e8255bea3ac68a124f7a445170d5b665eb39c17))
* **ci:** remove publishing patch ([#716](https://github.com/lithic-com/lithic-python/issues/716)) ([92f82b9](https://github.com/lithic-com/lithic-python/commit/92f82b9ccb0fc2b7e58aaa04220734ccf4f71976))

## 0.86.1 (2025-03-14)

Full Changelog: [v0.86.0...v0.86.1](https://github.com/lithic-com/lithic-python/compare/v0.86.0...v0.86.1)

### Bug Fixes

* **types:** handle more discriminated union shapes ([#713](https://github.com/lithic-com/lithic-python/issues/713)) ([eb8c941](https://github.com/lithic-com/lithic-python/commit/eb8c941ab542757530dc5ec9ff1eba7a89aeac74))


### Chores

* **internal:** bump rye to 0.44.0 ([#712](https://github.com/lithic-com/lithic-python/issues/712)) ([0ac2afe](https://github.com/lithic-com/lithic-python/commit/0ac2afe1892ff69251a97e92cae24bcd1532598f))
* **internal:** remove extra empty newlines ([#710](https://github.com/lithic-com/lithic-python/issues/710)) ([83aedda](https://github.com/lithic-com/lithic-python/commit/83aeddafa2aa3904f46017a026219d640a6c3da6))

## 0.86.0 (2025-03-12)

Full Changelog: [v0.85.0...v0.86.0](https://github.com/lithic-com/lithic-python/compare/v0.85.0...v0.86.0)

### Features

* **api:** new Settlement API endpoints and changes to update Account Holder endpoint ([#705](https://github.com/lithic-com/lithic-python/issues/705)) ([adccabb](https://github.com/lithic-com/lithic-python/commit/adccabbec1e63fe8bf74c18bdccc21c3f16ea142))
* **client:** allow passing `NotGiven` for body ([#697](https://github.com/lithic-com/lithic-python/issues/697)) ([0291f1f](https://github.com/lithic-com/lithic-python/commit/0291f1fa45b0813e995f042d4483c75324f03de0))
* **client:** update currency data type ([#709](https://github.com/lithic-com/lithic-python/issues/709)) ([b4a72ac](https://github.com/lithic-com/lithic-python/commit/b4a72ac8ad6c21f47d78f792b98364b500889e86))


### Bug Fixes

* **client:** mark some request bodies as optional ([0291f1f](https://github.com/lithic-com/lithic-python/commit/0291f1fa45b0813e995f042d4483c75324f03de0))
* **internal:** re-add portion of workflow to make CI happy ([d8c191f](https://github.com/lithic-com/lithic-python/commit/d8c191feaba90f6c0e3f1662610866dd382a6992))
* **internal:** skip failing transaction example ([df1bd93](https://github.com/lithic-com/lithic-python/commit/df1bd93a57fe01df54dc51476238523bf0c1ec54))


### Chores

* **api:** adds new `Internal` Category for FinancialTransactions ([#701](https://github.com/lithic-com/lithic-python/issues/701)) ([17c0aa5](https://github.com/lithic-com/lithic-python/commit/17c0aa5eccc116d6d24ff10b6b3500b632a3c000))
* **api:** release of Network Totals reporting and new filters for Velocity Limit Rules ([#708](https://github.com/lithic-com/lithic-python/issues/708)) ([e6dc1d1](https://github.com/lithic-com/lithic-python/commit/e6dc1d1739badfbc1bf58f477916c3a049b2b7d7))
* **client:** deprecate some fields ([b4a72ac](https://github.com/lithic-com/lithic-python/commit/b4a72ac8ad6c21f47d78f792b98364b500889e86))
* **docs:** update client docstring ([#703](https://github.com/lithic-com/lithic-python/issues/703)) ([a00fdff](https://github.com/lithic-com/lithic-python/commit/a00fdff57f4a593cb27ac988c08a18b7586ba690))
* **internal:** fix devcontainers setup ([#699](https://github.com/lithic-com/lithic-python/issues/699)) ([2a59b0b](https://github.com/lithic-com/lithic-python/commit/2a59b0be559f29d3da58658bd690a7f9d3a91d49))
* **internal:** properly set __pydantic_private__ ([#700](https://github.com/lithic-com/lithic-python/issues/700)) ([e7db283](https://github.com/lithic-com/lithic-python/commit/e7db283b63cc1158150e7067545de655a9236690))


### Documentation

* update some descriptions ([b4a72ac](https://github.com/lithic-com/lithic-python/commit/b4a72ac8ad6c21f47d78f792b98364b500889e86))
* update URLs from stainlessapi.com to stainless.com ([#702](https://github.com/lithic-com/lithic-python/issues/702)) ([84efefd](https://github.com/lithic-com/lithic-python/commit/84efefd92f231fec34d96845dcaf9a9ae2c4bd53))


### Refactors

* **client:** remove deprecated http client options ([#704](https://github.com/lithic-com/lithic-python/issues/704)) ([c745a2b](https://github.com/lithic-com/lithic-python/commit/c745a2b593ec7487810f0c5e4522e55e49602f4a))

## 0.85.0 (2025-02-13)

Full Changelog: [v0.84.0...v0.85.0](https://github.com/lithic-com/lithic-python/compare/v0.84.0...v0.85.0)

### Features

* **client:** send `X-Stainless-Read-Timeout` header ([#691](https://github.com/lithic-com/lithic-python/issues/691)) ([43d6692](https://github.com/lithic-com/lithic-python/commit/43d66921603b533dc9348da4f2bd1eb80826ecec))
* **pagination:** avoid fetching when has_more: false ([#693](https://github.com/lithic-com/lithic-python/issues/693)) ([705157b](https://github.com/lithic-com/lithic-python/commit/705157bd63c08bfa026647e8f90ab4fc90e46158))


### Bug Fixes

* asyncify on non-asyncio runtimes ([#696](https://github.com/lithic-com/lithic-python/issues/696)) ([41d8601](https://github.com/lithic-com/lithic-python/commit/41d8601b544757e7a7a0769245fbc5ca9142f442))


### Chores

* **api:** new 3DS Event and new `challenge_metadata` property on Authentications ([#695](https://github.com/lithic-com/lithic-python/issues/695)) ([f0dcb60](https://github.com/lithic-com/lithic-python/commit/f0dcb605baaa3f89e866182d84e001846428d955))
* **api:** new PaymentEventType for ACH Returns and small updates to 3DS AuthenticationResult ([#690](https://github.com/lithic-com/lithic-python/issues/690)) ([ab6b3e5](https://github.com/lithic-com/lithic-python/commit/ab6b3e5acb1e2f7614f60441b03348abf4217f19))
* **internal:** bummp ruff dependency ([#689](https://github.com/lithic-com/lithic-python/issues/689)) ([2d0fc56](https://github.com/lithic-com/lithic-python/commit/2d0fc56ef5c8b93e94a5dab4bf214f75dc8731f3))
* **internal:** change default timeout to an int ([#687](https://github.com/lithic-com/lithic-python/issues/687)) ([1bb4e70](https://github.com/lithic-com/lithic-python/commit/1bb4e70cc4afa33d8bf1861c31315dfe64eea0d2))
* **internal:** fix type traversing dictionary params ([#692](https://github.com/lithic-com/lithic-python/issues/692)) ([ad99873](https://github.com/lithic-com/lithic-python/commit/ad998734859dcbdae451a38bc26711a854f0edb7))
* **internal:** minor type handling changes ([#694](https://github.com/lithic-com/lithic-python/issues/694)) ([dfc6046](https://github.com/lithic-com/lithic-python/commit/dfc6046874c04b0873c555f6562208c328e74810))

## 0.84.0 (2025-01-28)

Full Changelog: [v0.83.0...v0.84.0](https://github.com/lithic-com/lithic-python/compare/v0.83.0...v0.84.0)

### Features

* **api:** adds additional request types for updating an Auth Rule ([#685](https://github.com/lithic-com/lithic-python/issues/685)) ([ed36107](https://github.com/lithic-com/lithic-python/commit/ed36107a5fa860fa1a87dfb73d58966759624b29))

## 0.83.0 (2025-01-24)

Full Changelog: [v0.82.0...v0.83.0](https://github.com/lithic-com/lithic-python/compare/v0.82.0...v0.83.0)

### Features

* **api:** adds additional fields to TransactionEvents ([#684](https://github.com/lithic-com/lithic-python/issues/684)) ([90da354](https://github.com/lithic-com/lithic-python/commit/90da35429ab778882fac77ba4e886c017d5f5b78))


### Chores

* **api:** additional field added to 3DS Responses and Tokenization ([#681](https://github.com/lithic-com/lithic-python/issues/681)) ([08d4bad](https://github.com/lithic-com/lithic-python/commit/08d4bade198e712e59a598fdb35bab06907d05a8))
* **internal:** minor formatting changes ([#683](https://github.com/lithic-com/lithic-python/issues/683)) ([3fd3619](https://github.com/lithic-com/lithic-python/commit/3fd3619639a433be49b8cdf27d0e92f8caaf0fe7))

## 0.82.0 (2025-01-21)

Full Changelog: [v0.81.1...v0.82.0](https://github.com/lithic-com/lithic-python/compare/v0.81.1...v0.82.0)

### ⚠ BREAKING CHANGES

* **types:** improve auth rules types ([#671](https://github.com/lithic-com/lithic-python/issues/671))
* **api:** removes AccountHolder `resubmit` endpoint and `KYC_ADVANCED` workflow ([#659](https://github.com/lithic-com/lithic-python/issues/659))

### Features

* **api:** removes AccountHolder `resubmit` endpoint and `KYC_ADVANCED` workflow ([#659](https://github.com/lithic-com/lithic-python/issues/659)) ([8b181ca](https://github.com/lithic-com/lithic-python/commit/8b181ca9ab1e09309d22f0c2de9ec41cb6b448dc))
* generate more types that are used as request bodies ([#649](https://github.com/lithic-com/lithic-python/issues/649)) ([413bb22](https://github.com/lithic-com/lithic-python/commit/413bb22511b1f28190eae3da910bac35fb1de841))
* **types:** improve auth rules types ([#671](https://github.com/lithic-com/lithic-python/issues/671)) ([5748bc0](https://github.com/lithic-com/lithic-python/commit/5748bc033592204bc983d8adea36df51b59671df))


### Bug Fixes

* **client:** only call .close() when needed ([#664](https://github.com/lithic-com/lithic-python/issues/664)) ([f6528df](https://github.com/lithic-com/lithic-python/commit/f6528dfd841d00157a50c9b0dbd9e4a61baae530))
* correctly handle deserialising `cls` fields ([#668](https://github.com/lithic-com/lithic-python/issues/668)) ([2ce887f](https://github.com/lithic-com/lithic-python/commit/2ce887f68604500c0c7ff0f5a0a3e2da6f9f7d02))
* reuse model in pagination items type ([#679](https://github.com/lithic-com/lithic-python/issues/679)) ([150965a](https://github.com/lithic-com/lithic-python/commit/150965ac048661778ba5becd99cdcde0903d5e71))
* **tests:** make test_get_platform less flaky ([#675](https://github.com/lithic-com/lithic-python/issues/675)) ([2dff4e0](https://github.com/lithic-com/lithic-python/commit/2dff4e0609c7226f61d7ff503c3d9a6abe08f895))


### Chores

* add back compat aliases for LineItemListResponse ([1e7eb6d](https://github.com/lithic-com/lithic-python/commit/1e7eb6daf16f95888ff30f020f954afd0faf55a3))
* add missing isclass check ([#661](https://github.com/lithic-com/lithic-python/issues/661)) ([e572151](https://github.com/lithic-com/lithic-python/commit/e572151d763b4ef9a27748bc0f6ddc088e35b29b))
* **api:** new ConvertPhysical endpoint to convert a virtual card to a physical card ([#656](https://github.com/lithic-com/lithic-python/issues/656)) ([6412dcd](https://github.com/lithic-com/lithic-python/commit/6412dcd78bae44cd35a742c357ec1e56948144e1))
* **api:** updates to documentation and additional filter for status on Transactions ([#669](https://github.com/lithic-com/lithic-python/issues/669)) ([2e69678](https://github.com/lithic-com/lithic-python/commit/2e69678de96264a5d2ba7b38cf07ffa76823e3f1))
* bump license year ([#660](https://github.com/lithic-com/lithic-python/issues/660)) ([b76a630](https://github.com/lithic-com/lithic-python/commit/b76a6307f08bc628e382638e33f07cac12160826))
* **docs:** updates documentation for DPANs ([#677](https://github.com/lithic-com/lithic-python/issues/677)) ([1fd8a18](https://github.com/lithic-com/lithic-python/commit/1fd8a184d28568eb4990a73746c440889325b6fa))
* **internal:** add support for TypeAliasType ([#652](https://github.com/lithic-com/lithic-python/issues/652)) ([988f2a0](https://github.com/lithic-com/lithic-python/commit/988f2a016c98cef5a3558c08f8568af27776a0fb))
* **internal:** avoid pytest-asyncio deprecation warning ([#676](https://github.com/lithic-com/lithic-python/issues/676)) ([f1a31f3](https://github.com/lithic-com/lithic-python/commit/f1a31f34ebe689b048f889b3ef0d470dc5defda4))
* **internal:** bump httpx dependency ([#662](https://github.com/lithic-com/lithic-python/issues/662)) ([767729e](https://github.com/lithic-com/lithic-python/commit/767729e44232516426fc018e9189e9a8d2ab48c5))
* **internal:** bump pyright ([#651](https://github.com/lithic-com/lithic-python/issues/651)) ([1406b81](https://github.com/lithic-com/lithic-python/commit/1406b81f7ca5e58d787afa86b723f4f271d361a4))
* **internal:** bump pyright dependency ([#672](https://github.com/lithic-com/lithic-python/issues/672)) ([77a255c](https://github.com/lithic-com/lithic-python/commit/77a255cb547c13d3b87127d096f628513dceb63f))
* **internal:** fix some typos ([#658](https://github.com/lithic-com/lithic-python/issues/658)) ([79baa5d](https://github.com/lithic-com/lithic-python/commit/79baa5d8fa228ee9f9575e264b8022e2c609f44a))
* **internal:** minor style changes ([#680](https://github.com/lithic-com/lithic-python/issues/680)) ([b1fb9fb](https://github.com/lithic-com/lithic-python/commit/b1fb9fbbe878bb1779db0ca23959565dcff929e1))
* **internal:** remove some duplicated imports ([#653](https://github.com/lithic-com/lithic-python/issues/653)) ([c446d74](https://github.com/lithic-com/lithic-python/commit/c446d74a9fd059d45d93966dd63894a68a76a965))
* **internal:** update deps ([#670](https://github.com/lithic-com/lithic-python/issues/670)) ([2eddffd](https://github.com/lithic-com/lithic-python/commit/2eddffdab2e6180f9f5b5f6848d3e8bbe45567fd))
* **internal:** update examples ([#663](https://github.com/lithic-com/lithic-python/issues/663)) ([7e704cf](https://github.com/lithic-com/lithic-python/commit/7e704cf7776ff4beb47beb397a846333c3843617))
* **internal:** updated imports ([#654](https://github.com/lithic-com/lithic-python/issues/654)) ([b0b1b64](https://github.com/lithic-com/lithic-python/commit/b0b1b644dcc1db989c22ba9def0fa4712e2e18d3))


### Documentation

* fix typos ([#665](https://github.com/lithic-com/lithic-python/issues/665)) ([b0de6d4](https://github.com/lithic-com/lithic-python/commit/b0de6d41f28cd60e8adfdcca389699a3c608156f))
* more typo fixes ([#666](https://github.com/lithic-com/lithic-python/issues/666)) ([f97e3bc](https://github.com/lithic-com/lithic-python/commit/f97e3bc55387ed862cf40d357051c896a28ad375))
* **raw responses:** fix duplicate `the` ([#674](https://github.com/lithic-com/lithic-python/issues/674)) ([9bc6a5e](https://github.com/lithic-com/lithic-python/commit/9bc6a5e8b9cbcb8e69497f4fef32f3ba2d7f2d1f))
* **readme:** example snippet for client context manager ([#657](https://github.com/lithic-com/lithic-python/issues/657)) ([4ca06b8](https://github.com/lithic-com/lithic-python/commit/4ca06b884448c3737fda47e1343814d20714d5ea))
* **readme:** fix misplaced period ([#667](https://github.com/lithic-com/lithic-python/issues/667)) ([51bdab7](https://github.com/lithic-com/lithic-python/commit/51bdab75952ec5716dab38b61c7c87cc8cda63fc))

## 0.81.1 (2024-12-11)

Full Changelog: [v0.81.0...v0.81.1](https://github.com/lithic-com/lithic-python/compare/v0.81.0...v0.81.1)

### Bug Fixes

* events.resend was missing v1 url prefix ([8c53c3c](https://github.com/lithic-com/lithic-python/commit/8c53c3c18f9ccefd64b722802521b35b84716f5d))


### Documentation

* **readme:** fix http client proxies example ([#647](https://github.com/lithic-com/lithic-python/issues/647)) ([8fac1ff](https://github.com/lithic-com/lithic-python/commit/8fac1ffdf8ebe994c02ac57b72a9fddc7c701b2e))

## 0.81.0 (2024-12-09)

Full Changelog: [v0.80.1...v0.81.0](https://github.com/lithic-com/lithic-python/compare/v0.80.1...v0.81.0)

### Features

* **api:** adds EventRuleResult to Transaction Events ([#646](https://github.com/lithic-com/lithic-python/issues/646)) ([51de0e6](https://github.com/lithic-com/lithic-python/commit/51de0e605212aef46aac02d5a45fa7f591630629))


### Chores

* **internal:** bump pydantic dependency ([#645](https://github.com/lithic-com/lithic-python/issues/645)) ([b55feb0](https://github.com/lithic-com/lithic-python/commit/b55feb0d12f89d50830ce285ae48e56fd129c7c2))
* **internal:** bump pyright ([#642](https://github.com/lithic-com/lithic-python/issues/642)) ([69d8957](https://github.com/lithic-com/lithic-python/commit/69d895702fe674b8554580e9346ad266b7057cb3))
* make the `Omit` type public ([#644](https://github.com/lithic-com/lithic-python/issues/644)) ([095008f](https://github.com/lithic-com/lithic-python/commit/095008f17b01d4cc0ec76cb0f84aaf0e5bdc60de))

## 0.80.1 (2024-11-28)

Full Changelog: [v0.80.0...v0.80.1](https://github.com/lithic-com/lithic-python/compare/v0.80.0...v0.80.1)

### Bug Fixes

* **client:** compat with new httpx 0.28.0 release ([#640](https://github.com/lithic-com/lithic-python/issues/640)) ([2e3c03d](https://github.com/lithic-com/lithic-python/commit/2e3c03d072a9c4a8a3d76414c3d1a64b5359f057))

## 0.80.0 (2024-11-28)

Full Changelog: [v0.79.1...v0.80.0](https://github.com/lithic-com/lithic-python/compare/v0.79.1...v0.80.0)

### Features

* **api:** updates to Auth Rules numeric types, new Card Types and Authorization Rule Backtests ([#637](https://github.com/lithic-com/lithic-python/issues/637)) ([6436634](https://github.com/lithic-com/lithic-python/commit/6436634a1a0ccc9b6ec070c2553bdb45ab656dd6))


### Chores

* **api:** add backtest methods to AuthRules ([#638](https://github.com/lithic-com/lithic-python/issues/638)) ([8125eac](https://github.com/lithic-com/lithic-python/commit/8125eac6b6bb5e448f8641c362a334f0eab5a5fa))
* **internal:** exclude mypy from running on tests ([#639](https://github.com/lithic-com/lithic-python/issues/639)) ([9ad6f0b](https://github.com/lithic-com/lithic-python/commit/9ad6f0bbf8ffc74641f018adaa1cc99e80be1d12))
* **internal:** fix compat model_dump method when warnings are passed ([#633](https://github.com/lithic-com/lithic-python/issues/633)) ([eb6c135](https://github.com/lithic-com/lithic-python/commit/eb6c135106a0e11e15aa6245db72a019ea90668e))
* remove now unused `cached-property` dep ([#636](https://github.com/lithic-com/lithic-python/issues/636)) ([78321ef](https://github.com/lithic-com/lithic-python/commit/78321efbac2e6da20afb852d6bf38fa371751d99))


### Documentation

* add info log level to readme ([#635](https://github.com/lithic-com/lithic-python/issues/635)) ([aed46f6](https://github.com/lithic-com/lithic-python/commit/aed46f67456c19cf389275607f593e8e269e3237))

## 0.79.1 (2024-11-18)

Full Changelog: [v0.79.0...v0.79.1](https://github.com/lithic-com/lithic-python/compare/v0.79.0...v0.79.1)

### Bug Fixes

* **asyncify:** avoid hanging process under certain conditions ([#632](https://github.com/lithic-com/lithic-python/issues/632)) ([a588059](https://github.com/lithic-com/lithic-python/commit/a588059fb8e877c9b174ce665991c5ade57dc49d))


### Chores

* **tests:** limit array example length ([#630](https://github.com/lithic-com/lithic-python/issues/630)) ([015e1cb](https://github.com/lithic-com/lithic-python/commit/015e1cb414358c2a90a21453d1854328caa0d968))

## 0.79.0 (2024-11-14)

Full Changelog: [v0.78.1...v0.79.0](https://github.com/lithic-com/lithic-python/compare/v0.78.1...v0.79.0)

### Features

* **api:** adds PrimeRates API ([#628](https://github.com/lithic-com/lithic-python/issues/628)) ([f0a2272](https://github.com/lithic-com/lithic-python/commit/f0a22728c090d593b483c562c61adaa71cd0221e))

## 0.78.1 (2024-11-12)

Full Changelog: [v0.78.0...v0.78.1](https://github.com/lithic-com/lithic-python/compare/v0.78.0...v0.78.1)

### Bug Fixes

* don't use dicts as iterables in transform ([#627](https://github.com/lithic-com/lithic-python/issues/627)) ([717c8a9](https://github.com/lithic-com/lithic-python/commit/717c8a97db21965f95299cc97cfd96a16960ed18))


### Chores

* **api:** add business_account_token param for listing Balances ([#625](https://github.com/lithic-com/lithic-python/issues/625)) ([7513850](https://github.com/lithic-com/lithic-python/commit/75138504756e0cf60fb86f04b2ced22351325d13))
* **api:** adds replacement_account_token to Card create parameters ([#623](https://github.com/lithic-com/lithic-python/issues/623)) ([79071df](https://github.com/lithic-com/lithic-python/commit/79071df7bd89ecf6f1fe887a5a8a45a75345efc1))
* **internal:** cleanup duplicate import ([#624](https://github.com/lithic-com/lithic-python/issues/624)) ([d067e5e](https://github.com/lithic-com/lithic-python/commit/d067e5e7a10b4f229e3a6c0dbed3de879771f1c3))
* **tests:** adjust retry timeout values ([#621](https://github.com/lithic-com/lithic-python/issues/621)) ([1a732a9](https://github.com/lithic-com/lithic-python/commit/1a732a9d3c0bdce3603f005a4b49f252d495dd85))


### Documentation

* move comments in example snippets ([#626](https://github.com/lithic-com/lithic-python/issues/626)) ([d49933a](https://github.com/lithic-com/lithic-python/commit/d49933a2c275ca79599e7884f8d6dfe82b3c7ae6))

## 0.78.0 (2024-11-05)

Full Changelog: [v0.77.2...v0.78.0](https://github.com/lithic-com/lithic-python/compare/v0.77.2...v0.78.0)

### ⚠ BREAKING CHANGES

* **api:** removes AuthRules V1 ([#620](https://github.com/lithic-com/lithic-python/issues/620))

### Features

* **api:** removes AuthRules V1 ([#620](https://github.com/lithic-com/lithic-python/issues/620)) ([e415592](https://github.com/lithic-com/lithic-python/commit/e41559205443f329cd17f3e3da51b7f429c3f7f5))
* **project:** drop support for Python 3.7 ([#618](https://github.com/lithic-com/lithic-python/issues/618)) ([733aa30](https://github.com/lithic-com/lithic-python/commit/733aa30202e4766bbb8ed7af54a8e5e0a32ee9b4))

## 0.77.2 (2024-11-04)

Full Changelog: [v0.77.1...v0.77.2](https://github.com/lithic-com/lithic-python/compare/v0.77.1...v0.77.2)

### Bug Fixes

* support json safe serialization for basemodel subclasses ([#616](https://github.com/lithic-com/lithic-python/issues/616)) ([be1d3e3](https://github.com/lithic-com/lithic-python/commit/be1d3e37630d91b600da7399d5871c3479f0ab98))

## 0.77.1 (2024-11-02)

Full Changelog: [v0.77.0...v0.77.1](https://github.com/lithic-com/lithic-python/compare/v0.77.0...v0.77.1)

### Bug Fixes

* don't use dicts as iterables in transform ([#615](https://github.com/lithic-com/lithic-python/issues/615)) ([65456d4](https://github.com/lithic-com/lithic-python/commit/65456d4c5131474d7c37232f0f09f4e497e1da80))


### Chores

* **api:** adds `charge_off` functionality to FinancialAccounts ([#613](https://github.com/lithic-com/lithic-python/issues/613)) ([44895bb](https://github.com/lithic-com/lithic-python/commit/44895bb85c8ad0bf84c606312a0006e2a4312fe3))
* **docs:** updates to documentation for V2 AuthRules ([#611](https://github.com/lithic-com/lithic-python/issues/611)) ([8931217](https://github.com/lithic-com/lithic-python/commit/8931217fd1d63933098b570d427af45e2c9e92cd))
* **internal:** bump mypy ([#614](https://github.com/lithic-com/lithic-python/issues/614)) ([717b3f3](https://github.com/lithic-com/lithic-python/commit/717b3f3e45cae0b30468109c99278c6969b28a6e))

## 0.77.0 (2024-10-28)

Full Changelog: [v0.76.0...v0.77.0](https://github.com/lithic-com/lithic-python/compare/v0.76.0...v0.77.0)

### Features

* **api:** updates ([#610](https://github.com/lithic-com/lithic-python/issues/610)) ([4cc66a9](https://github.com/lithic-com/lithic-python/commit/4cc66a96b0eb15481c4164ec900f3470bae3b840))


### Chores

* **api:** add `PIN_BLOCKED` to `detailed_results` property on Event ([#606](https://github.com/lithic-com/lithic-python/issues/606)) ([ac9985f](https://github.com/lithic-com/lithic-python/commit/ac9985f9f1fefb9fae7db90f8095492db0cff738))
* **api:** adds new result types to Transactions and Events ([#608](https://github.com/lithic-com/lithic-python/issues/608)) ([ff13e35](https://github.com/lithic-com/lithic-python/commit/ff13e35c1f4d760c34d870a5f6da972c57d4968a))
* **internal:** bump pytest to v8 & pydantic ([#609](https://github.com/lithic-com/lithic-python/issues/609)) ([a2641b7](https://github.com/lithic-com/lithic-python/commit/a2641b71894a9aa078314f56d51f4625df837685))

## 0.76.0 (2024-10-23)

Full Changelog: [v0.75.0...v0.76.0](https://github.com/lithic-com/lithic-python/compare/v0.75.0...v0.76.0)

### Features

* **api:** add `interest_details` properties to LoanTapes ([#604](https://github.com/lithic-com/lithic-python/issues/604)) ([365001b](https://github.com/lithic-com/lithic-python/commit/365001ba8a147e1f9c5547e19305163693e1f5ed))

## 0.75.0 (2024-10-22)

Full Changelog: [v0.74.1...v0.75.0](https://github.com/lithic-com/lithic-python/compare/v0.74.1...v0.75.0)

### Features

* **api:** removes `transfer_transaction.created` webhook and updates to VerificationApplication ([#603](https://github.com/lithic-com/lithic-python/issues/603)) ([b387f32](https://github.com/lithic-com/lithic-python/commit/b387f32b6922b6318273ce15bca3f5cdf1992b1e))


### Chores

* **internal:** remove unused black config ([#601](https://github.com/lithic-com/lithic-python/issues/601)) ([73a28e5](https://github.com/lithic-com/lithic-python/commit/73a28e5071d404ef16d69ae3d153789a4c4b1208))

## 0.74.1 (2024-10-21)

Full Changelog: [v0.74.0...v0.74.1](https://github.com/lithic-com/lithic-python/compare/v0.74.0...v0.74.1)

### Bug Fixes

* **client/async:** correctly retry in all cases ([#600](https://github.com/lithic-com/lithic-python/issues/600)) ([d0f302c](https://github.com/lithic-com/lithic-python/commit/d0f302cfe00945ab5722982059e9dd529b5185d2))


### Chores

* **internal:** bump ruff dependency ([#599](https://github.com/lithic-com/lithic-python/issues/599)) ([dbc528b](https://github.com/lithic-com/lithic-python/commit/dbc528be4ae82d0808f217562b98579b6361a401))
* **internal:** update test syntax ([#597](https://github.com/lithic-com/lithic-python/issues/597)) ([65c3fef](https://github.com/lithic-com/lithic-python/commit/65c3fef432217abbc707687389377a28dea5c511))

## 0.74.0 (2024-10-11)

Full Changelog: [v0.73.0...v0.74.0](https://github.com/lithic-com/lithic-python/compare/v0.73.0...v0.74.0)

### Features

* **api:** updates to documentation and addition of new 3DS simulation methods ([#595](https://github.com/lithic-com/lithic-python/issues/595)) ([041dc26](https://github.com/lithic-com/lithic-python/commit/041dc265c1943e8186e2901533129159dae99348))

## 0.73.0 (2024-10-09)

Full Changelog: [v0.72.1...v0.73.0](https://github.com/lithic-com/lithic-python/compare/v0.72.1...v0.73.0)

### Features

* **api:** small updates to Documents, AccountHolders and LoanTapes ([#594](https://github.com/lithic-com/lithic-python/issues/594)) ([7011e2d](https://github.com/lithic-com/lithic-python/commit/7011e2daf1bd763a1fb795657b98b98e2b47d08a))


### Chores

* add repr to PageInfo class ([#592](https://github.com/lithic-com/lithic-python/issues/592)) ([39f389b](https://github.com/lithic-com/lithic-python/commit/39f389b88edcd503a3747c59cf3a3c960cf7dc7c))

## 0.72.1 (2024-10-07)

Full Changelog: [v0.72.0...v0.72.1](https://github.com/lithic-com/lithic-python/compare/v0.72.0...v0.72.1)

### Bug Fixes

* **client:** avoid OverflowError with very large retry counts ([#591](https://github.com/lithic-com/lithic-python/issues/591)) ([aa81a86](https://github.com/lithic-com/lithic-python/commit/aa81a8699e8832bd79ed0ab04e7de299b89ecb41))


### Chores

* **api:** small updates to verification addresses and Statement and LoanTape fields ([#588](https://github.com/lithic-com/lithic-python/issues/588)) ([98d9c01](https://github.com/lithic-com/lithic-python/commit/98d9c019116591254e1595a932ebc54f88e8c323))
* **internal:** add support for parsing bool response content ([#590](https://github.com/lithic-com/lithic-python/issues/590)) ([1cb2aa4](https://github.com/lithic-com/lithic-python/commit/1cb2aa44f9259d6ae834554ac10b016f56c89313))

## 0.72.0 (2024-10-01)

Full Changelog: [v0.71.0...v0.72.0](https://github.com/lithic-com/lithic-python/compare/v0.71.0...v0.72.0)

### Features

* **api:** rename `loan_tape_response.statement_balance` to `previous_statement_balance` ([#587](https://github.com/lithic-com/lithic-python/issues/587)) ([57b648e](https://github.com/lithic-com/lithic-python/commit/57b648e29e213d87b395421e5571f9b89cd640f1))


### Documentation

* fix typo in fenced code block language ([#586](https://github.com/lithic-com/lithic-python/issues/586)) ([5e8dbb4](https://github.com/lithic-com/lithic-python/commit/5e8dbb42879f28d8437f7b8634c375ee8a8095e7))
* improve and reference contributing documentation ([#584](https://github.com/lithic-com/lithic-python/issues/584)) ([aa350d9](https://github.com/lithic-com/lithic-python/commit/aa350d92d0a722303e24de3baedd2e4a126db583))

## 0.71.0 (2024-10-01)

Full Changelog: [v0.70.0...v0.71.0](https://github.com/lithic-com/lithic-python/compare/v0.70.0...v0.71.0)

### Features

* **api:** add Management Operations and Loan Tapes API ([#582](https://github.com/lithic-com/lithic-python/issues/582)) ([34cdf6a](https://github.com/lithic-com/lithic-python/commit/34cdf6a68e8eecc1b0d78c9d9dcc1dc197ef3d66))

## 0.70.0 (2024-09-25)

Full Changelog: [v0.69.0...v0.70.0](https://github.com/lithic-com/lithic-python/compare/v0.69.0...v0.70.0)

### Features

* **api:** adds endpoint for migrating auth rules from v1 to V2. marks v1 auth rules as deprecated ([#581](https://github.com/lithic-com/lithic-python/issues/581)) ([71cfe49](https://github.com/lithic-com/lithic-python/commit/71cfe4931afb9baa511cd61a17f454dc0ab534cf))
* **client:** allow overriding retry count header ([#580](https://github.com/lithic-com/lithic-python/issues/580)) ([ee6b2a9](https://github.com/lithic-com/lithic-python/commit/ee6b2a941b12d1b49fe080d053be5e800628de18))


### Chores

* **internal:** use `typing_extensions.overload` instead of `typing` ([#578](https://github.com/lithic-com/lithic-python/issues/578)) ([186a97c](https://github.com/lithic-com/lithic-python/commit/186a97c2d44ba71b7528b478d20e695fcce4f174))

## 0.69.0 (2024-09-24)

Full Changelog: [v0.68.0...v0.69.0](https://github.com/lithic-com/lithic-python/compare/v0.68.0...v0.69.0)

### Features

* **api:** add `ACCOUNT_DELINQUENT` to `detailed_results` enum ([#576](https://github.com/lithic-com/lithic-python/issues/576)) ([b4f8760](https://github.com/lithic-com/lithic-python/commit/b4f87609de5ba24d05778c87f7fae71ae21a01bd))

## 0.68.0 (2024-09-23)

Full Changelog: [v0.67.0...v0.68.0](https://github.com/lithic-com/lithic-python/compare/v0.67.0...v0.68.0)

### Features

* **api:** add `canceled` to `transaction_status` enum values ([#575](https://github.com/lithic-com/lithic-python/issues/575)) ([d10002b](https://github.com/lithic-com/lithic-python/commit/d10002bc752692bd81d4f0af527d36ddb06e5c40))


### Chores

* **internal:** update pydantic v1 compat helpers ([#573](https://github.com/lithic-com/lithic-python/issues/573)) ([90fa3a1](https://github.com/lithic-com/lithic-python/commit/90fa3a1e0393271448cf808a7157cfc0734d6ecf))

## 0.67.0 (2024-09-19)

Full Changelog: [v0.66.2...v0.67.0](https://github.com/lithic-com/lithic-python/compare/v0.66.2...v0.67.0)

### ⚠ BREAKING CHANGES

* **api:** update model `FinancialAccount` ([#572](https://github.com/lithic-com/lithic-python/issues/572))

### Features

* **api:** update model `FinancialAccount` ([#572](https://github.com/lithic-com/lithic-python/issues/572)) ([6b056cb](https://github.com/lithic-com/lithic-python/commit/6b056cbb34fbaf67194d1739d582d4951306c589))
* **client:** send retry count header ([#570](https://github.com/lithic-com/lithic-python/issues/570)) ([c65ffea](https://github.com/lithic-com/lithic-python/commit/c65ffea747bd137142f61da9605cf4483f456604))

## 0.66.2 (2024-09-19)

Full Changelog: [v0.66.1...v0.66.2](https://github.com/lithic-com/lithic-python/compare/v0.66.1...v0.66.2)

### Bug Fixes

* **client:** handle domains with underscores ([#568](https://github.com/lithic-com/lithic-python/issues/568)) ([82cdfb0](https://github.com/lithic-com/lithic-python/commit/82cdfb06be0e282d90853b64924dd5ae5f7c8d11))

## 0.66.1 (2024-09-18)

Full Changelog: [v0.66.0...v0.66.1](https://github.com/lithic-com/lithic-python/compare/v0.66.0...v0.66.1)

### Chores

* **internal:** specify API version for each endpoints instead of hardcoded in base URLs ([#565](https://github.com/lithic-com/lithic-python/issues/565)) ([ad2d835](https://github.com/lithic-com/lithic-python/commit/ad2d83572ced963baa45eb99d43750b9e89b523a))
* **tests:** fix get_embed_url to specify /v1/ prefix ([f84ec12](https://github.com/lithic-com/lithic-python/commit/f84ec125a08f95c526bddf6130588a5ee340547b))

## 0.66.0 (2024-09-17)

Full Changelog: [v0.65.0...v0.66.0](https://github.com/lithic-com/lithic-python/compare/v0.65.0...v0.66.0)

### ⚠ BREAKING CHANGES

* **api:** updates book transfer status, updates to transactions, add currency model ([#564](https://github.com/lithic-com/lithic-python/issues/564))

### Features

* **api:** updates book transfer status, updates to transactions, add currency model ([#564](https://github.com/lithic-com/lithic-python/issues/564)) ([49a3a63](https://github.com/lithic-com/lithic-python/commit/49a3a631806d3327535511f27173f48f95628927))


### Chores

* add docstrings to raw response properties ([#558](https://github.com/lithic-com/lithic-python/issues/558)) ([15eec4c](https://github.com/lithic-com/lithic-python/commit/15eec4cbdfeaa5a94b49732f8dbbec4a85fcfb83))
* **internal:** bump pyright / mypy version ([#563](https://github.com/lithic-com/lithic-python/issues/563)) ([325561c](https://github.com/lithic-com/lithic-python/commit/325561c6d8892397c6072765a06ee6e5f52d08f0))
* **internal:** bump ruff ([#562](https://github.com/lithic-com/lithic-python/issues/562)) ([8a34fc1](https://github.com/lithic-com/lithic-python/commit/8a34fc12683c70a2bd623db503f09f78ab612baf))


### Documentation

* **readme:** add section on determining installed version ([#560](https://github.com/lithic-com/lithic-python/issues/560)) ([05ba523](https://github.com/lithic-com/lithic-python/commit/05ba523f6c882d5627998119624f15a593d9d3c8))
* update CONTRIBUTING.md ([#561](https://github.com/lithic-com/lithic-python/issues/561)) ([1ac232c](https://github.com/lithic-com/lithic-python/commit/1ac232c528d0e45425be75af244c2aafa916d165))

## 0.65.0 (2024-09-06)

Full Changelog: [v0.64.0...v0.65.0](https://github.com/lithic-com/lithic-python/compare/v0.64.0...v0.65.0)

### Features

* **api:** add tier and state to financial_accounts ([#557](https://github.com/lithic-com/lithic-python/issues/557)) ([9bad05b](https://github.com/lithic-com/lithic-python/commit/9bad05bb6a9973bcc6bc627b1568e93f25c0d0e5))


### Chores

* **docs:** update description for postal codes ([#556](https://github.com/lithic-com/lithic-python/issues/556)) ([993f718](https://github.com/lithic-com/lithic-python/commit/993f718f25d45e56e1736c757329b28981bc3866))
* pyproject.toml formatting changes ([#553](https://github.com/lithic-com/lithic-python/issues/553)) ([e1cb673](https://github.com/lithic-com/lithic-python/commit/e1cb673600044649d4027a86620eccfcae88e4b4))
* **test:** change test name ([#555](https://github.com/lithic-com/lithic-python/issues/555)) ([ada39fe](https://github.com/lithic-com/lithic-python/commit/ada39fea44d9bee99a6b64c4ce72085e4dcbae99))

## 0.64.0 (2024-09-03)

Full Changelog: [v0.63.0...v0.64.0](https://github.com/lithic-com/lithic-python/compare/v0.63.0...v0.64.0)

### Features

* **api:** declare AccountHolderBusinessResponse and remove entity_token from BusinessEntity ([#551](https://github.com/lithic-com/lithic-python/issues/551)) ([6e6aff0](https://github.com/lithic-com/lithic-python/commit/6e6aff04db80cc58ebd32c1531147639b8bd1d83))

## 0.63.0 (2024-08-29)

Full Changelog: [v0.62.0...v0.63.0](https://github.com/lithic-com/lithic-python/compare/v0.62.0...v0.63.0)

### ⚠ BREAKING CHANGES

* **api:** add shared model Document ([#549](https://github.com/lithic-com/lithic-python/issues/549))

### Features

* **api:** add shared model Document ([#549](https://github.com/lithic-com/lithic-python/issues/549)) ([f8195c8](https://github.com/lithic-com/lithic-python/commit/f8195c87414265fe2955fdc773a88981c771bcfc))

## 0.62.0 (2024-08-28)

Full Changelog: [v0.61.0...v0.62.0](https://github.com/lithic-com/lithic-python/compare/v0.61.0...v0.62.0)

### Features

* **api:** add 'pin status' and 'pending_commands' to Card model ([#548](https://github.com/lithic-com/lithic-python/issues/548)) ([659ecca](https://github.com/lithic-com/lithic-python/commit/659ecca973405b11f78fd04b9f57c01574fa5e09))


### Chores

* **docs:** minor edits ([#546](https://github.com/lithic-com/lithic-python/issues/546)) ([ae3ebc5](https://github.com/lithic-com/lithic-python/commit/ae3ebc5885874122a2f444bcf1f2e004885adb6b))

## 0.61.0 (2024-08-23)

Full Changelog: [v0.60.0...v0.61.0](https://github.com/lithic-com/lithic-python/compare/v0.60.0...v0.61.0)

### Features

* **api:** add endpoints and webhooks for 3DS challenge decisions and challenges ([#544](https://github.com/lithic-com/lithic-python/issues/544)) ([c5437be](https://github.com/lithic-com/lithic-python/commit/c5437be23dd46461391419ca02e5a63c62ac1d81))

## 0.60.0 (2024-08-23)

Full Changelog: [v0.59.0...v0.60.0](https://github.com/lithic-com/lithic-python/compare/v0.59.0...v0.60.0)

### Features

* **api:** new book_transfer_transaction events and Settlement Report field deprecations ([#542](https://github.com/lithic-com/lithic-python/issues/542)) ([2e73d68](https://github.com/lithic-com/lithic-python/commit/2e73d68e66378b75c3069635c9a7375113b3dbb0))

## 0.59.0 (2024-08-20)

Full Changelog: [v0.58.0...v0.59.0](https://github.com/lithic-com/lithic-python/compare/v0.58.0...v0.59.0)

### Features

* **api:** add property `next_payment_end_date` and `next_payment_due_date` to Statement model ([#541](https://github.com/lithic-com/lithic-python/issues/541)) ([eba1a51](https://github.com/lithic-com/lithic-python/commit/eba1a51e018b4acc7ba5d6b3989309fd01e8b18b))


### Chores

* **ci:** also run pydantic v1 tests ([#540](https://github.com/lithic-com/lithic-python/issues/540)) ([c48e5c4](https://github.com/lithic-com/lithic-python/commit/c48e5c472c802ab5dae8e64aa618285fd082e146))
* **client:** fix parsing union responses when non-json is returned ([#539](https://github.com/lithic-com/lithic-python/issues/539)) ([139cfd8](https://github.com/lithic-com/lithic-python/commit/139cfd890603c29a11c58c0b605e0234c4a35bcd))
* **docs:** update state description on Card ([#537](https://github.com/lithic-com/lithic-python/issues/537)) ([73f607e](https://github.com/lithic-com/lithic-python/commit/73f607ec9f8c662a4254bfb11db7a5c1da537efc))

## 0.58.0 (2024-08-16)

Full Changelog: [v0.57.0...v0.58.0](https://github.com/lithic-com/lithic-python/compare/v0.57.0...v0.58.0)

### Features

* **api:** add StatementListParams property include_initial_statements ([#536](https://github.com/lithic-com/lithic-python/issues/536)) ([6a24d16](https://github.com/lithic-com/lithic-python/commit/6a24d1651e83b778c1d6d9a13c40f5e0f0c232f5))


### Chores

* **internal:** use different 32bit detection method ([#534](https://github.com/lithic-com/lithic-python/issues/534)) ([1e1f813](https://github.com/lithic-com/lithic-python/commit/1e1f8134789f1af66b5a719c339643256c37e89f))

## 0.57.0 (2024-08-14)

Full Changelog: [v0.56.0...v0.57.0](https://github.com/lithic-com/lithic-python/compare/v0.56.0...v0.57.0)

### Features

* **api:** add SettlementReport property `is_complete` ([#533](https://github.com/lithic-com/lithic-python/issues/533)) ([cd57de3](https://github.com/lithic-com/lithic-python/commit/cd57de388f103180e76e29774d98543ba9bcbf99))


### Chores

* **examples:** minor formatting changes ([#532](https://github.com/lithic-com/lithic-python/issues/532)) ([1094602](https://github.com/lithic-com/lithic-python/commit/109460229154cf71f28bf15550b7d1694dea3acb))
* **internal:** update some imports ([#530](https://github.com/lithic-com/lithic-python/issues/530)) ([10a7b9a](https://github.com/lithic-com/lithic-python/commit/10a7b9ad72308394e6318610c5bb1f5ad1a99b76))

## 0.56.0 (2024-08-12)

Full Changelog: [v0.55.0...v0.56.0](https://github.com/lithic-com/lithic-python/compare/v0.55.0...v0.56.0)

### Features

* **api:** add property `Account.cardholder_currency` ([#529](https://github.com/lithic-com/lithic-python/issues/529)) ([26f0669](https://github.com/lithic-com/lithic-python/commit/26f0669a8efe806df97dbb91836d00bdd51a0564))
* **api:** add property `Card.cardholder_currency` ([26f0669](https://github.com/lithic-com/lithic-python/commit/26f0669a8efe806df97dbb91836d00bdd51a0564))
* **api:** add property `CardProgram.cardholder_currencies` ([26f0669](https://github.com/lithic-com/lithic-python/commit/26f0669a8efe806df97dbb91836d00bdd51a0564))
* **api:** add property `CardProgram.cardholder_currency` ([26f0669](https://github.com/lithic-com/lithic-python/commit/26f0669a8efe806df97dbb91836d00bdd51a0564))


### Chores

* **ci:** bump prism mock server version ([#526](https://github.com/lithic-com/lithic-python/issues/526)) ([c610f81](https://github.com/lithic-com/lithic-python/commit/c610f8115d65667e99f373946ba44357dde506c7))
* **internal:** ensure package is importable in lint cmd ([#528](https://github.com/lithic-com/lithic-python/issues/528)) ([194b0d7](https://github.com/lithic-com/lithic-python/commit/194b0d720fd9f01e12705e7792a2dfdcafefa44b))

## 0.55.0 (2024-08-09)

Full Changelog: [v0.54.0...v0.55.0](https://github.com/lithic-com/lithic-python/compare/v0.54.0...v0.55.0)

### ⚠ BREAKING CHANGES

* **api:** rename property 'financial_accounts.statement.AccountStanding.state' to 'period_state' ([#525](https://github.com/lithic-com/lithic-python/issues/525))

### Features

* **api:** add event type 'card.reissued' ([#521](https://github.com/lithic-com/lithic-python/issues/521)) ([87e7ab3](https://github.com/lithic-com/lithic-python/commit/87e7ab36383282e64d12422574c8f95929165324))
* **api:** add methods to simulate enrollment review and enrollment document review ([#523](https://github.com/lithic-com/lithic-python/issues/523)) ([4e4515f](https://github.com/lithic-com/lithic-python/commit/4e4515f793f0d2004156ebbc86741716e01778ad))
* **api:** rename property 'financial_accounts.statement.AccountStanding.state' to 'period_state' ([#525](https://github.com/lithic-com/lithic-python/issues/525)) ([909ecac](https://github.com/lithic-com/lithic-python/commit/909ecace7a7c00b2bcf9deb13a05d8e3642f9356))


### Chores

* **internal:** bump ruff version ([#519](https://github.com/lithic-com/lithic-python/issues/519)) ([bba5c95](https://github.com/lithic-com/lithic-python/commit/bba5c95e67449658db54a1d8e79fb0063b5ff0a8))
* **internal:** update pydantic compat helper function ([#522](https://github.com/lithic-com/lithic-python/issues/522)) ([99d987f](https://github.com/lithic-com/lithic-python/commit/99d987f2887abcd9005377f7491a4da228ad082f))
* **internal:** updates ([#524](https://github.com/lithic-com/lithic-python/issues/524)) ([9645382](https://github.com/lithic-com/lithic-python/commit/964538237afaa3073af632e4363d059aaba29427))

## 0.54.0 (2024-08-05)

Full Changelog: [v0.53.1...v0.54.0](https://github.com/lithic-com/lithic-python/compare/v0.53.1...v0.54.0)

### Features

* **api:** add event type 'statements.created' ([#518](https://github.com/lithic-com/lithic-python/issues/518)) ([2dd6b21](https://github.com/lithic-com/lithic-python/commit/2dd6b21b40b9387900b75061c35bb391aeb7f790))
* **client:** add `retries_taken` to raw response class ([#514](https://github.com/lithic-com/lithic-python/issues/514)) ([2d797d0](https://github.com/lithic-com/lithic-python/commit/2d797d0f7451d48a427d8d0429cf01244865385f))


### Chores

* add transactions example ([#515](https://github.com/lithic-com/lithic-python/issues/515)) ([7a53618](https://github.com/lithic-com/lithic-python/commit/7a53618d7455fca0f7b8202a0702ef9f7924563b))
* **ci:** run transactions example ([#517](https://github.com/lithic-com/lithic-python/issues/517)) ([76054d7](https://github.com/lithic-com/lithic-python/commit/76054d72a5ff1e2eeed60aedd8fcd9ea845691a3))
* **internal:** bump pyright ([#513](https://github.com/lithic-com/lithic-python/issues/513)) ([c79e2e8](https://github.com/lithic-com/lithic-python/commit/c79e2e840db333844aebf72fe2107babcc1786bf))
* **internal:** test updates ([#516](https://github.com/lithic-com/lithic-python/issues/516)) ([dc4b527](https://github.com/lithic-com/lithic-python/commit/dc4b5270d33c1c4c21200f5f336ec84b35c441f0))
* **internal:** use `TypeAlias` marker for type assignments ([#511](https://github.com/lithic-com/lithic-python/issues/511)) ([d339158](https://github.com/lithic-com/lithic-python/commit/d339158b8caa71cfd52e09417b8e14e3e59d4ec4))

## 0.53.1 (2024-07-29)

Full Changelog: [v0.53.0...v0.53.1](https://github.com/lithic-com/lithic-python/compare/v0.53.0...v0.53.1)

### Bug Fixes

* **client:** correctly apply client level timeout for account holders ([#510](https://github.com/lithic-com/lithic-python/issues/510)) ([9ec85e1](https://github.com/lithic-com/lithic-python/commit/9ec85e1938eac38b15b729734bcd5b54ea41aebb))


### Chores

* **internal:** add type construction helper ([#508](https://github.com/lithic-com/lithic-python/issues/508)) ([a0cfd29](https://github.com/lithic-com/lithic-python/commit/a0cfd29050d60cae1d8c2fb5f48b71973b57f76c))

## 0.53.0 (2024-07-26)

Full Changelog: [v0.52.0...v0.53.0](https://github.com/lithic-com/lithic-python/compare/v0.52.0...v0.53.0)

### Features

* **api:** add method to fetch the extended credit for a given credit product ([#507](https://github.com/lithic-com/lithic-python/issues/507)) ([fb874a3](https://github.com/lithic-com/lithic-python/commit/fb874a30fd7d197d61797e0b4b764d6808689b61))


### Chores

* **docs:** set of improvements ([#505](https://github.com/lithic-com/lithic-python/issues/505)) ([501a976](https://github.com/lithic-com/lithic-python/commit/501a976aded81e32ef3d32f87fbda44c772a72a1))

## 0.52.0 (2024-07-23)

Full Changelog: [v0.51.0...v0.52.0](https://github.com/lithic-com/lithic-python/compare/v0.51.0...v0.52.0)

### ⚠ BREAKING CHANGES

* **api:** deprecate 'auth rule token' in 'card' and 'account holder' models ([#504](https://github.com/lithic-com/lithic-python/issues/504))

### Features

* **api:** deprecate 'auth rule token' in 'card' and 'account holder' models ([#504](https://github.com/lithic-com/lithic-python/issues/504)) ([9cf5402](https://github.com/lithic-com/lithic-python/commit/9cf5402a24342280b2c84804111afa7258f5f5e8))


### Chores

* **tests:** update prism version ([#503](https://github.com/lithic-com/lithic-python/issues/503)) ([dddf991](https://github.com/lithic-com/lithic-python/commit/dddf9912af30d785cab29ae5145c0d0452ceed6a))


### Documentation

* **readme:** fix example snippet imports ([#501](https://github.com/lithic-com/lithic-python/issues/501)) ([c037ec0](https://github.com/lithic-com/lithic-python/commit/c037ec0e646fd2b3d0d51c74d4cecdd330fd4aef))

## 0.51.0 (2024-07-19)

Full Changelog: [v0.50.0...v0.51.0](https://github.com/lithic-com/lithic-python/compare/v0.50.0...v0.51.0)

### Features

* **api:** add method to retrieve a transaction's enhanced commercial data ([#500](https://github.com/lithic-com/lithic-python/issues/500)) ([f0662e9](https://github.com/lithic-com/lithic-python/commit/f0662e94eb1fdb0d7b6213fcae5482c2cabf2322))


### Chores

* **ci:** limit release doctor target branches ([#499](https://github.com/lithic-com/lithic-python/issues/499)) ([4fa41c9](https://github.com/lithic-com/lithic-python/commit/4fa41c93f84847ca0e89ea4a474712798e0cf3a8))
* **docs:** document how to do per-request http client customization ([#497](https://github.com/lithic-com/lithic-python/issues/497)) ([bae139d](https://github.com/lithic-com/lithic-python/commit/bae139d73fa75f9a76c09f6bae6f1fd697679eee))

## 0.50.0 (2024-07-17)

Full Changelog: [v0.49.0...v0.50.0](https://github.com/lithic-com/lithic-python/compare/v0.49.0...v0.50.0)

### Features

* **api:** updates ([#496](https://github.com/lithic-com/lithic-python/issues/496)) ([09c15d3](https://github.com/lithic-com/lithic-python/commit/09c15d3599e699d8510c8946d6cb5b12089b2292))


### Chores

* **docs:** minor update to formatting of API link in README ([#495](https://github.com/lithic-com/lithic-python/issues/495)) ([4f1dd78](https://github.com/lithic-com/lithic-python/commit/4f1dd786d3f4973c34cf1b47fa6d18bb28815ecb))
* **internal:** minor options / compat functions updates ([#493](https://github.com/lithic-com/lithic-python/issues/493)) ([05b1935](https://github.com/lithic-com/lithic-python/commit/05b1935597ecb49c9730df2f6117617da71af210))

## 0.49.0 (2024-07-11)

Full Changelog: [v0.48.6...v0.49.0](https://github.com/lithic-com/lithic-python/compare/v0.48.6...v0.49.0)

### Features

* **api:** param 'financial_account_token' for 'external_bank_accounts.create()' is now required ([#491](https://github.com/lithic-com/lithic-python/issues/491)) ([1b8968d](https://github.com/lithic-com/lithic-python/commit/1b8968d86dd8d9d1f17a624f7e43669c6874a760))

## 0.48.6 (2024-07-11)

Full Changelog: [v0.48.5...v0.48.6](https://github.com/lithic-com/lithic-python/compare/v0.48.5...v0.48.6)

### Chores

* **ci:** also run workflows for PRs targeting `next` ([#487](https://github.com/lithic-com/lithic-python/issues/487)) ([dd74e55](https://github.com/lithic-com/lithic-python/commit/dd74e5533fac8962ff69837c177462721a4a8710))
* **ci:** update rye to v0.35.0 ([#482](https://github.com/lithic-com/lithic-python/issues/482)) ([30f2c5b](https://github.com/lithic-com/lithic-python/commit/30f2c5b716e74cae4178267b4959496c33fe5335))
* **internal:** add helper function ([#485](https://github.com/lithic-com/lithic-python/issues/485)) ([e688304](https://github.com/lithic-com/lithic-python/commit/e6883042caa64572f8fcb06fcc1ba6db823c652c))
* **internal:** minor import restructuring ([#488](https://github.com/lithic-com/lithic-python/issues/488)) ([10206cf](https://github.com/lithic-com/lithic-python/commit/10206cfb133a0631f011638eb8b746d08a8eb67f))
* **internal:** minor request options handling changes ([#484](https://github.com/lithic-com/lithic-python/issues/484)) ([1f8293c](https://github.com/lithic-com/lithic-python/commit/1f8293cc4e4a1bea29c21ccfe715edc7acdf53c7))
* **internal:** update mypy ([#486](https://github.com/lithic-com/lithic-python/issues/486)) ([f05d7a1](https://github.com/lithic-com/lithic-python/commit/f05d7a17bac4ea11826b7117283b218368b88592))


### Documentation

* **examples:** use named params more ([#490](https://github.com/lithic-com/lithic-python/issues/490)) ([f42beef](https://github.com/lithic-com/lithic-python/commit/f42beef8c98751bc2d64b02253eb4c9c14759422))

## 0.48.5 (2024-07-02)

Full Changelog: [v0.48.4...v0.48.5](https://github.com/lithic-com/lithic-python/compare/v0.48.4...v0.48.5)

### Bug Fixes

* **client:** always respect content-type multipart/form-data if provided ([#481](https://github.com/lithic-com/lithic-python/issues/481)) ([cb58f98](https://github.com/lithic-com/lithic-python/commit/cb58f9816cb9ebc88f8d00aadc77140eb3afbae9))


### Chores

* gitignore test server logs ([#478](https://github.com/lithic-com/lithic-python/issues/478)) ([333ec59](https://github.com/lithic-com/lithic-python/commit/333ec59ef57c99e92b47e5508acd79fa9f0ce4dc))
* **internal:** add helper method for constructing `BaseModel`s ([#480](https://github.com/lithic-com/lithic-python/issues/480)) ([037c807](https://github.com/lithic-com/lithic-python/commit/037c80726879b13c983f458c6f5f6a78176c9ec1))
* **internal:** add reflection helper function ([#476](https://github.com/lithic-com/lithic-python/issues/476)) ([4d84125](https://github.com/lithic-com/lithic-python/commit/4d841255b4ada2f1315f292f6a869550b4db7477))
* **internal:** add rich as a dev dependency ([#479](https://github.com/lithic-com/lithic-python/issues/479)) ([a7843c1](https://github.com/lithic-com/lithic-python/commit/a7843c146f920484fd75e6a94d2310cb6cd5d0d9))

## 0.48.4 (2024-06-27)

Full Changelog: [v0.48.3...v0.48.4](https://github.com/lithic-com/lithic-python/compare/v0.48.3...v0.48.4)

### Chores

* **deps:** bump anyio to v4.4.0 ([#474](https://github.com/lithic-com/lithic-python/issues/474)) ([13d1520](https://github.com/lithic-com/lithic-python/commit/13d1520aac5539f2ee7f1a5e8c89d76fc452025b))

## 0.48.3 (2024-06-27)

Full Changelog: [v0.48.2...v0.48.3](https://github.com/lithic-com/lithic-python/compare/v0.48.2...v0.48.3)

### Bug Fixes

* **build:** include more files in sdist builds ([#472](https://github.com/lithic-com/lithic-python/issues/472)) ([9f173fd](https://github.com/lithic-com/lithic-python/commit/9f173fdcf6f3db1e937ae90fbcf7b850b87479c7))

## 0.48.2 (2024-06-26)

Full Changelog: [v0.48.1...v0.48.2](https://github.com/lithic-com/lithic-python/compare/v0.48.1...v0.48.2)

### Bug Fixes

* temporarily patch upstream version to fix broken release flow ([#470](https://github.com/lithic-com/lithic-python/issues/470)) ([ca18455](https://github.com/lithic-com/lithic-python/commit/ca1845557fc0c28fb48857092dd06e8d8e540540))

## 0.48.1 (2024-06-25)

Full Changelog: [v0.48.0...v0.48.1](https://github.com/lithic-com/lithic-python/compare/v0.48.0...v0.48.1)

### Bug Fixes

* **docs:** fix link to advanced python httpx docs ([#469](https://github.com/lithic-com/lithic-python/issues/469)) ([f1683b5](https://github.com/lithic-com/lithic-python/commit/f1683b57a0ed2c810f61833d8675923252bd9e2b))


### Chores

* formatting ([#467](https://github.com/lithic-com/lithic-python/issues/467)) ([4754798](https://github.com/lithic-com/lithic-python/commit/47547988ccef6b3b4b141c31c76f6a7a05366be4))

## 0.48.0 (2024-06-21)

Full Changelog: [v0.47.0...v0.48.0](https://github.com/lithic-com/lithic-python/compare/v0.47.0...v0.48.0)

### ⚠ BREAKING CHANGES

* **api:** remove unused event type 'statement.created'
* **api:** remove unused business account type
* **api:** remove unused embed request params type
* **api:** updates ([#466](https://github.com/lithic-com/lithic-python/issues/466))

### Features

* **api:** add 'reverse' method for book transfers ([0e94cdb](https://github.com/lithic-com/lithic-python/commit/0e94cdb2e8acf61560aa56def695acdbe982f4f6))
* **api:** add field 'trace numbers' to payment method attribute model ([0e94cdb](https://github.com/lithic-com/lithic-python/commit/0e94cdb2e8acf61560aa56def695acdbe982f4f6))
* **api:** remove unused business account type ([0e94cdb](https://github.com/lithic-com/lithic-python/commit/0e94cdb2e8acf61560aa56def695acdbe982f4f6))
* **api:** remove unused embed request params type ([0e94cdb](https://github.com/lithic-com/lithic-python/commit/0e94cdb2e8acf61560aa56def695acdbe982f4f6))
* **api:** remove unused event type 'statement.created' ([0e94cdb](https://github.com/lithic-com/lithic-python/commit/0e94cdb2e8acf61560aa56def695acdbe982f4f6))
* **api:** updates ([#466](https://github.com/lithic-com/lithic-python/issues/466)) ([0e94cdb](https://github.com/lithic-com/lithic-python/commit/0e94cdb2e8acf61560aa56def695acdbe982f4f6))


### Bug Fixes

* **client/async:** avoid blocking io call for platform headers ([#465](https://github.com/lithic-com/lithic-python/issues/465)) ([67c2ce2](https://github.com/lithic-com/lithic-python/commit/67c2ce23c63f599a3fe1eedf1e777099599fe4df))


### Chores

* **internal:** add a `default_query` method ([#463](https://github.com/lithic-com/lithic-python/issues/463)) ([37cd9bd](https://github.com/lithic-com/lithic-python/commit/37cd9bd8459b9f3856cc168a52b6a9032906dedb))

## 0.47.0 (2024-06-12)

Full Changelog: [v0.46.0...v0.47.0](https://github.com/lithic-com/lithic-python/compare/v0.46.0...v0.47.0)

### Features

* **api:** updates ([#460](https://github.com/lithic-com/lithic-python/issues/460)) ([f685c2d](https://github.com/lithic-com/lithic-python/commit/f685c2dbe5931a73a4e747228930f298270116fc))

## 0.46.0 (2024-06-05)

Full Changelog: [v0.45.0...v0.46.0](https://github.com/lithic-com/lithic-python/compare/v0.45.0...v0.46.0)

### ⚠ BREAKING CHANGES

* **api:** remove some endpoints and other API updates ([#458](https://github.com/lithic-com/lithic-python/issues/458))

### Features

* **api:** remove some endpoints and other API updates ([#458](https://github.com/lithic-com/lithic-python/issues/458)) ([378e64e](https://github.com/lithic-com/lithic-python/commit/378e64e62cb91c45a3d6bdf3c2ccc21a66d4b1de))

## 0.45.0 (2024-05-30)

Full Changelog: [v0.44.0...v0.45.0](https://github.com/lithic-com/lithic-python/compare/v0.44.0...v0.45.0)

### Features

* **api:** update detailed_results enum values ([#456](https://github.com/lithic-com/lithic-python/issues/456)) ([16837ea](https://github.com/lithic-com/lithic-python/commit/16837ea02d6782bd8f3b8446199507f59947d6b0))

## 0.44.0 (2024-05-29)

Full Changelog: [v0.43.0...v0.44.0](https://github.com/lithic-com/lithic-python/compare/v0.43.0...v0.44.0)

### Features

* **api:** add simulate_receipt and simulate_action endpoints ([#454](https://github.com/lithic-com/lithic-python/issues/454)) ([d7058ec](https://github.com/lithic-com/lithic-python/commit/d7058ec8baa28401874770232408571c0fe8e81d))

## 0.43.0 (2024-05-29)

Full Changelog: [v0.42.0...v0.43.0](https://github.com/lithic-com/lithic-python/compare/v0.42.0...v0.43.0)

### Features

* **api:** updates ([#453](https://github.com/lithic-com/lithic-python/issues/453)) ([3c46bf1](https://github.com/lithic-com/lithic-python/commit/3c46bf1f48a8fbd78f2f9061e7524d0159f022f4))


### Chores

* **ci:** update rye install location ([#448](https://github.com/lithic-com/lithic-python/issues/448)) ([a7361a5](https://github.com/lithic-com/lithic-python/commit/a7361a5cccf2c82ecc92e0ec14d37ece1ada41db))
* **ci:** update rye install location ([#449](https://github.com/lithic-com/lithic-python/issues/449)) ([f5b5e22](https://github.com/lithic-com/lithic-python/commit/f5b5e226244c65febf50fc15cc9cde9c6f33046b))
* **docs:** add SECURITY.md ([#444](https://github.com/lithic-com/lithic-python/issues/444)) ([a3ff562](https://github.com/lithic-com/lithic-python/commit/a3ff562896feabf54cf8cc419842c92f7cfbf041))
* **internal:** add slightly better logging to scripts ([#446](https://github.com/lithic-com/lithic-python/issues/446)) ([e0478b3](https://github.com/lithic-com/lithic-python/commit/e0478b3f8918168b520bf13c6442c1ba1fa8b6ce))
* **internal:** bump pydantic dependency ([#445](https://github.com/lithic-com/lithic-python/issues/445)) ([007cfaa](https://github.com/lithic-com/lithic-python/commit/007cfaa3f9fde230ee77eb6f3f9a1bfacdf37f75))
* **internal:** bump pyright ([#450](https://github.com/lithic-com/lithic-python/issues/450)) ([3b790a6](https://github.com/lithic-com/lithic-python/commit/3b790a66bccbbdc2392ffe1a11808a1cbb298333))
* **internal:** update bootstrap script ([#452](https://github.com/lithic-com/lithic-python/issues/452)) ([066564f](https://github.com/lithic-com/lithic-python/commit/066564fa9559635f374ae51deadf48c6cfc68e9d))
* **tests:** update some example values ([#447](https://github.com/lithic-com/lithic-python/issues/447)) ([b88c2a4](https://github.com/lithic-com/lithic-python/commit/b88c2a47f7aa06fc88a017087927a1677838be66))


### Documentation

* **contributing:** update references to rye-up.com ([#451](https://github.com/lithic-com/lithic-python/issues/451)) ([7ac824e](https://github.com/lithic-com/lithic-python/commit/7ac824e027eae3c81827cdaae8c301a95610c95d))
* **readme:** fix misleading timeout example value ([#439](https://github.com/lithic-com/lithic-python/issues/439)) ([74afd3f](https://github.com/lithic-com/lithic-python/commit/74afd3f4fa1706b789b4e3899e9b7c18d525555a))

## 0.42.0 (2024-05-01)

Full Changelog: [v0.41.0...v0.42.0](https://github.com/lithic-com/lithic-python/compare/v0.41.0...v0.42.0)

### Features

* **api:** changes to balance-related return types and other API changes ([#432](https://github.com/lithic-com/lithic-python/issues/432)) ([a7045b1](https://github.com/lithic-com/lithic-python/commit/a7045b18518c8524d75bc7539a08f431de21dff1))
* **api:** updates ([#419](https://github.com/lithic-com/lithic-python/issues/419)) ([70be79c](https://github.com/lithic-com/lithic-python/commit/70be79c6d6370a179805800fbfa5903f29cd8d2d))
* **api:** updates ([#421](https://github.com/lithic-com/lithic-python/issues/421)) ([5657004](https://github.com/lithic-com/lithic-python/commit/56570041949e6b3f61bdea419d6eb3df6b1cd494))
* **api:** updates ([#438](https://github.com/lithic-com/lithic-python/issues/438)) ([48a5562](https://github.com/lithic-com/lithic-python/commit/48a5562c2336f2bbb9058631eb22ff83d58a1464))
* **models:** add to_dict & to_json helper methods ([#416](https://github.com/lithic-com/lithic-python/issues/416)) ([49d5ba1](https://github.com/lithic-com/lithic-python/commit/49d5ba184b2c331b9bdb2d2057ea8971a1646251))


### Bug Fixes

* **docs:** doc improvements ([#428](https://github.com/lithic-com/lithic-python/issues/428)) ([549737f](https://github.com/lithic-com/lithic-python/commit/549737f387bab6ed63fd0ee6bdcdc3bb8aab90a4))


### Chores

* **client:** log response headers in debug mode ([#435](https://github.com/lithic-com/lithic-python/issues/435)) ([6310797](https://github.com/lithic-com/lithic-python/commit/6310797ea884b2592bc3aa7e3d976161981d34e5))
* fix typo ([#418](https://github.com/lithic-com/lithic-python/issues/418)) ([79d8921](https://github.com/lithic-com/lithic-python/commit/79d8921b342b72f34a813d03aa2726c8ddc2eeb6))
* **internal:** add lru_cache helper function ([#422](https://github.com/lithic-com/lithic-python/issues/422)) ([e7a7f23](https://github.com/lithic-com/lithic-python/commit/e7a7f23bd73227a02909f4b34bd434690ac263c4))
* **internal:** add scripts/test, scripts/mock and add ci job ([#436](https://github.com/lithic-com/lithic-python/issues/436)) ([26b4052](https://github.com/lithic-com/lithic-python/commit/26b4052d88bdbecaaca9bc796860cb064273a466))
* **internal:** ban usage of lru_cache ([#423](https://github.com/lithic-com/lithic-python/issues/423)) ([b72c88f](https://github.com/lithic-com/lithic-python/commit/b72c88f3cb92ffa9cf8b7f7798c276f540ccbc93))
* **internal:** bump mock server version to ~5.8.0 ([#437](https://github.com/lithic-com/lithic-python/issues/437)) ([c9d79b4](https://github.com/lithic-com/lithic-python/commit/c9d79b4aad101d69599230b7c842e6da236ef164))
* **internal:** bump pyright to 1.1.359 ([#424](https://github.com/lithic-com/lithic-python/issues/424)) ([7cbc60f](https://github.com/lithic-com/lithic-python/commit/7cbc60fe6fd23dec9c6c631b8cc9d8695d5eea52))
* **internal:** formatting ([#420](https://github.com/lithic-com/lithic-python/issues/420)) ([d6dcfe6](https://github.com/lithic-com/lithic-python/commit/d6dcfe6654c607541348850c465578f2c4a32836))
* **internal:** minor reformatting ([#434](https://github.com/lithic-com/lithic-python/issues/434)) ([fb1f85c](https://github.com/lithic-com/lithic-python/commit/fb1f85cfd0dba0c21cd870d007dee66a4320623b))
* **internal:** reformat imports ([#433](https://github.com/lithic-com/lithic-python/issues/433)) ([f22b15e](https://github.com/lithic-com/lithic-python/commit/f22b15e326a5d3acb8845ee77ae8f52b5e48d602))
* **internal:** restructure imports ([#425](https://github.com/lithic-com/lithic-python/issues/425)) ([9d9ab1c](https://github.com/lithic-com/lithic-python/commit/9d9ab1cf28d02f0ad29e06ef29f2466d14b399c2))
* **internal:** update test helper function ([#431](https://github.com/lithic-com/lithic-python/issues/431)) ([4c2b592](https://github.com/lithic-com/lithic-python/commit/4c2b59227c0762bbe8ed435ea7cf3f3f4f4949c5))
* **internal:** use actions/checkout@v4 for codeflow ([#430](https://github.com/lithic-com/lithic-python/issues/430)) ([4afd494](https://github.com/lithic-com/lithic-python/commit/4afd49407732feb69de3f21d73fa658e85e02548))
* rename resource types ([#427](https://github.com/lithic-com/lithic-python/issues/427)) ([9afd708](https://github.com/lithic-com/lithic-python/commit/9afd70880749914dccd8224880712447f60a7a5f))
* **tests:** rename test file ([#429](https://github.com/lithic-com/lithic-python/issues/429)) ([20380e1](https://github.com/lithic-com/lithic-python/commit/20380e119f9ea9b67daf94e6d9709335195f7942))

## 0.41.0 (2024-04-08)

Full Changelog: [v0.40.0...v0.41.0](https://github.com/lithic-com/lithic-python/compare/v0.40.0...v0.41.0)

### Features

* **api:** add detailed result CARD_NOT_ACTIVATED ([#413](https://github.com/lithic-com/lithic-python/issues/413)) ([c0f2fc0](https://github.com/lithic-com/lithic-python/commit/c0f2fc07dde12c057a821be2ba1c0ec102011203))
* **api:** add event type digital_wallet.tokenization_two_factor_authentication_code_sent ([#409](https://github.com/lithic-com/lithic-python/issues/409)) ([2431cc1](https://github.com/lithic-com/lithic-python/commit/2431cc1f59d269be9f8f669e918a991b21387e45))
* **api:** add params spend_limit and spend_velocity ([#412](https://github.com/lithic-com/lithic-python/issues/412)) ([40d9cce](https://github.com/lithic-com/lithic-python/commit/40d9ccec81edd8eb71d53c6e8ee131991fc0385f))
* **api:** add settlement_report.updated enum ([#402](https://github.com/lithic-com/lithic-python/issues/402)) ([49b6566](https://github.com/lithic-com/lithic-python/commit/49b656605a41fbeb328c1b5bbee6b0a2c3e32540))
* **api:** update financial transaction status enum ([#405](https://github.com/lithic-com/lithic-python/issues/405)) ([5978972](https://github.com/lithic-com/lithic-python/commit/5978972745d8cc0ee045beb346f85a24def68a00))
* **api:** update link to encrypted PIN block docs ([#414](https://github.com/lithic-com/lithic-python/issues/414)) ([aefe04e](https://github.com/lithic-com/lithic-python/commit/aefe04e0a3e574bd9dc41097df9c3cd593793f41))
* **api:** updates ([#403](https://github.com/lithic-com/lithic-python/issues/403)) ([a1f9274](https://github.com/lithic-com/lithic-python/commit/a1f9274e360c09fe9aedf3b91dabbc1dbfad8348))
* **client:** add DefaultHttpxClient and DefaultAsyncHttpxClient ([#415](https://github.com/lithic-com/lithic-python/issues/415)) ([d264e68](https://github.com/lithic-com/lithic-python/commit/d264e6833705cef6bba38eb704a53545e4fac3ad))
* **package:** export default constants ([#404](https://github.com/lithic-com/lithic-python/issues/404)) ([aadd2c5](https://github.com/lithic-com/lithic-python/commit/aadd2c558ee1823c5e41218712a25c627bf1f8d3))


### Bug Fixes

* **project:** use absolute github links on PyPi ([#406](https://github.com/lithic-com/lithic-python/issues/406)) ([cf279ff](https://github.com/lithic-com/lithic-python/commit/cf279ffc9f52062a1011e1f627c25f1e0af44a95))
* revert regression with 3.7 support ([#401](https://github.com/lithic-com/lithic-python/issues/401)) ([ca50938](https://github.com/lithic-com/lithic-python/commit/ca509385a92c741d1751582d9d252961de85edcd))


### Chores

* **client:** validate that max_retries is not None ([#408](https://github.com/lithic-com/lithic-python/issues/408)) ([a073786](https://github.com/lithic-com/lithic-python/commit/a073786f15200692bde119fa4c64403fddd40fa4))
* **internal:** defer model build for import latency ([#410](https://github.com/lithic-com/lithic-python/issues/410)) ([48a5b9a](https://github.com/lithic-com/lithic-python/commit/48a5b9a23841d68342e9119663a4f088d2fa9beb))
* **internal:** streaming updates ([#411](https://github.com/lithic-com/lithic-python/issues/411)) ([42944ef](https://github.com/lithic-com/lithic-python/commit/42944ef792adce6767e7da50dcf596b45a857412))


### Documentation

* **contributing:** fix typo ([#397](https://github.com/lithic-com/lithic-python/issues/397)) ([f6ecbee](https://github.com/lithic-com/lithic-python/commit/f6ecbee5c10edec9e1fb5391ce3a22f0fd95d4ad))

## 0.40.0 (2024-03-21)

Full Changelog: [v0.39.0...v0.40.0](https://github.com/lithic-com/lithic-python/compare/v0.39.0...v0.40.0)

### Features

* **api:** adds closed state ([#396](https://github.com/lithic-com/lithic-python/issues/396)) ([ce9d732](https://github.com/lithic-com/lithic-python/commit/ce9d732ec90e776b5eea0e77bc880d662921d639))
* **api:** updates ([#395](https://github.com/lithic-com/lithic-python/issues/395)) ([911d3e2](https://github.com/lithic-com/lithic-python/commit/911d3e24e30e6409e68a44389b58d3be18f7053a))


### Performance Improvements

* cache TypeAdapters ([#389](https://github.com/lithic-com/lithic-python/issues/389)) ([16f35fa](https://github.com/lithic-com/lithic-python/commit/16f35fad0bc1f250028991635f39ee34c29c450a))


### Chores

* add back examples ([e0eba72](https://github.com/lithic-com/lithic-python/commit/e0eba7230c6256a2b90ea1de7a9e814f80da4398))
* add back removed code ([36c5c4e](https://github.com/lithic-com/lithic-python/commit/36c5c4e84ee61ca9b9cae51d95c7e9bb1906eec2))
* **client:** improve error message for invalid http_client argument ([#380](https://github.com/lithic-com/lithic-python/issues/380)) ([0ea3801](https://github.com/lithic-com/lithic-python/commit/0ea38014e414fd60fd461992b52743ce8499ba66))
* **docs:** add back custom readme code ([23a52b2](https://github.com/lithic-com/lithic-python/commit/23a52b28bcab6293ff4b3a212dbc389026c62a08))
* **docs:** mention install from git repo ([#377](https://github.com/lithic-com/lithic-python/issues/377)) ([8b6e48c](https://github.com/lithic-com/lithic-python/commit/8b6e48c5f72df0f8380dbde642ccb31c809c9e30))
* **docs:** temporarily remove custom readme code ([#387](https://github.com/lithic-com/lithic-python/issues/387)) ([93530fd](https://github.com/lithic-com/lithic-python/commit/93530fdc4b004c6ec353a550b9641e37a898c1ef))
* export NOT_GIVEN sentinel value ([#384](https://github.com/lithic-com/lithic-python/issues/384)) ([841497f](https://github.com/lithic-com/lithic-python/commit/841497faed8a1b22adf6a724eb5b7e936276974e))
* **internal:** add core support for deserializing into number response ([#381](https://github.com/lithic-com/lithic-python/issues/381)) ([cb5e9d2](https://github.com/lithic-com/lithic-python/commit/cb5e9d27a6bacf861921e49b30cc1abee365530a))
* **internal:** bump pyright ([#382](https://github.com/lithic-com/lithic-python/issues/382)) ([8aad846](https://github.com/lithic-com/lithic-python/commit/8aad846ffad52816d6ee55ca64aaf3b92649998d))
* **internal:** formatting change ([#394](https://github.com/lithic-com/lithic-python/issues/394)) ([b9ede81](https://github.com/lithic-com/lithic-python/commit/b9ede81a7b936794160ece4abb9c33e6e41c0285))
* **internal:** improve deserialisation of discriminated unions ([#385](https://github.com/lithic-com/lithic-python/issues/385)) ([9062866](https://github.com/lithic-com/lithic-python/commit/9062866fa7aa87f9f5c25c401638415ea4986a09))
* **internal:** loosen input type for util function ([#392](https://github.com/lithic-com/lithic-python/issues/392)) ([1294d5b](https://github.com/lithic-com/lithic-python/commit/1294d5b6766a15dd5956395324dd38ded94adcb0))
* **internal:** minor core client restructuring ([#374](https://github.com/lithic-com/lithic-python/issues/374)) ([bca5b1c](https://github.com/lithic-com/lithic-python/commit/bca5b1c9b5f65743883ca48b54de22bffd7c6560))
* **internal:** split up transforms into sync / async ([#378](https://github.com/lithic-com/lithic-python/issues/378)) ([0cecc63](https://github.com/lithic-com/lithic-python/commit/0cecc6324700a8d1b38222ff032b5f492a0e663b))
* **internal:** support more input types ([#379](https://github.com/lithic-com/lithic-python/issues/379)) ([0cde41d](https://github.com/lithic-com/lithic-python/commit/0cde41d7d8850d1d6bca08fdc1358241d62779de))
* **internal:** support parsing Annotated types ([#383](https://github.com/lithic-com/lithic-python/issues/383)) ([ded4ec2](https://github.com/lithic-com/lithic-python/commit/ded4ec2ef0ea794238b1658a989701b24d53d465))
* **internal:** update generated pragma comment ([#391](https://github.com/lithic-com/lithic-python/issues/391)) ([cac2a8b](https://github.com/lithic-com/lithic-python/commit/cac2a8b1319904b4d07a7864d426284ebd557d63))
* temporarily remove examples for migration ([644a601](https://github.com/lithic-com/lithic-python/commit/644a601cf2c271e5e3c3aff0a5084f14b0e1fb74))
* temporarily remove various code as part of refactor ([#388](https://github.com/lithic-com/lithic-python/issues/388)) ([306df73](https://github.com/lithic-com/lithic-python/commit/306df733bf153bf89931060cf2c5d9aa170c86ed))


### Documentation

* **contributing:** improve wording ([#376](https://github.com/lithic-com/lithic-python/issues/376)) ([ea83617](https://github.com/lithic-com/lithic-python/commit/ea836172c1533eea4008732215b72d3f8ef0065d))
* fix typo in CONTRIBUTING.md ([#390](https://github.com/lithic-com/lithic-python/issues/390)) ([2fc74c2](https://github.com/lithic-com/lithic-python/commit/2fc74c260e3166ed92c7613f6952604b253d6607))
* **readme:** document how to make undocumented requests ([#393](https://github.com/lithic-com/lithic-python/issues/393)) ([0fb722f](https://github.com/lithic-com/lithic-python/commit/0fb722fe212c67cdcab814ba68158c74607c94f6))

## 0.39.0 (2024-02-27)

Full Changelog: [v0.38.0...v0.39.0](https://github.com/lithic-com/lithic-python/compare/v0.38.0...v0.39.0)

### Features

* **api:** updates ([#373](https://github.com/lithic-com/lithic-python/issues/373)) ([08870a1](https://github.com/lithic-com/lithic-python/commit/08870a180f77cbe69ee0a4dfebc48fa5346592ff))


### Chores

* **client:** use anyio.sleep instead of asyncio.sleep ([#372](https://github.com/lithic-com/lithic-python/issues/372)) ([203870e](https://github.com/lithic-com/lithic-python/commit/203870e2370fc57ac29eb3dea41501d6115fcd8d))
* **internal:** bump pyright ([#370](https://github.com/lithic-com/lithic-python/issues/370)) ([f048d0e](https://github.com/lithic-com/lithic-python/commit/f048d0e187f072f030ac647cd2e0da9e41c5eeb6))

## 0.38.0 (2024-02-23)

Full Changelog: [v0.37.0...v0.38.0](https://github.com/lithic-com/lithic-python/compare/v0.37.0...v0.38.0)

### Features

* **api:** tokenizations ([#369](https://github.com/lithic-com/lithic-python/issues/369)) ([87b5088](https://github.com/lithic-com/lithic-python/commit/87b5088f84a6b200636f80b56d9a188a0e9d66a5))


### Chores

* **internal:** update deps ([#367](https://github.com/lithic-com/lithic-python/issues/367)) ([2e8ddb7](https://github.com/lithic-com/lithic-python/commit/2e8ddb70724b9000d652ec2863e997d087ffb73d))

## 0.37.0 (2024-02-21)

Full Changelog: [v0.36.0...v0.37.0](https://github.com/lithic-com/lithic-python/compare/v0.36.0...v0.37.0)

### Features

* **api:** create financial account and retry microdeposits endpoints ([#366](https://github.com/lithic-com/lithic-python/issues/366)) ([4cc06ec](https://github.com/lithic-com/lithic-python/commit/4cc06eca313e87524174d9b6af615e36c8f5c8dd))


### Chores

* **internal:** bump rye to v0.24.0 ([#364](https://github.com/lithic-com/lithic-python/issues/364)) ([ef3b396](https://github.com/lithic-com/lithic-python/commit/ef3b396cfb9f58894506514e889d78168a246489))

## 0.36.0 (2024-02-19)

Full Changelog: [v0.35.0...v0.36.0](https://github.com/lithic-com/lithic-python/compare/v0.35.0...v0.36.0)

### Features

* **api:** update financial_account_type and documentation ([#363](https://github.com/lithic-com/lithic-python/issues/363)) ([589dd28](https://github.com/lithic-com/lithic-python/commit/589dd28a38513e4627237868d25de960ce0a9d52))


### Chores

* **internal:** refactor release environment script ([#361](https://github.com/lithic-com/lithic-python/issues/361)) ([6da0145](https://github.com/lithic-com/lithic-python/commit/6da0145a8b54d879fb3f3401562761014035ec5e))
* **tests:** add integration test for pagination ([#358](https://github.com/lithic-com/lithic-python/issues/358)) ([8aafef9](https://github.com/lithic-com/lithic-python/commit/8aafef98237f52c61da023db201392df09acb7b8))


### Documentation

* add CONTRIBUTING.md ([#360](https://github.com/lithic-com/lithic-python/issues/360)) ([e37f886](https://github.com/lithic-com/lithic-python/commit/e37f886e638f29ec150615e345ec76bcf7f1532d))

## 0.35.0 (2024-02-07)

Full Changelog: [v0.34.2...v0.35.0](https://github.com/lithic-com/lithic-python/compare/v0.34.2...v0.35.0)

### Features

* **api:** updates ([#356](https://github.com/lithic-com/lithic-python/issues/356)) ([1d9d6c7](https://github.com/lithic-com/lithic-python/commit/1d9d6c739a458b6ac8af595fba5f11a2c2fd325f))

## 0.34.2 (2024-02-06)

Full Changelog: [v0.34.1...v0.34.2](https://github.com/lithic-com/lithic-python/compare/v0.34.1...v0.34.2)

### Bug Fixes

* **types:** loosen most List params types to Iterable ([#355](https://github.com/lithic-com/lithic-python/issues/355)) ([9d94f70](https://github.com/lithic-com/lithic-python/commit/9d94f706b111d82a7fb517ee0215d877754ba690))


### Chores

* **internal:** add lint command ([#354](https://github.com/lithic-com/lithic-python/issues/354)) ([2874d3b](https://github.com/lithic-com/lithic-python/commit/2874d3bfe4aab6c726893c8c31fc6fb8bcf45571))
* **internal:** support serialising iterable types ([#352](https://github.com/lithic-com/lithic-python/issues/352)) ([a09d15c](https://github.com/lithic-com/lithic-python/commit/a09d15c2a3feb9226513d7b598e238de096ba996))

## 0.34.1 (2024-02-04)

Full Changelog: [v0.34.0...v0.34.1](https://github.com/lithic-com/lithic-python/compare/v0.34.0...v0.34.1)

### Bug Fixes

* prevent crash when platform.architecture() is not allowed ([#351](https://github.com/lithic-com/lithic-python/issues/351)) ([fc7fd7b](https://github.com/lithic-com/lithic-python/commit/fc7fd7be6ec4a6e874bb515db810b2d539be8757))


### Chores

* **interal:** make link to api.md relative ([#349](https://github.com/lithic-com/lithic-python/issues/349)) ([f85a5e0](https://github.com/lithic-com/lithic-python/commit/f85a5e0b9cb599967951781dfe22801280b9c40f))

## 0.34.0 (2024-01-31)

Full Changelog: [v0.33.0...v0.34.0](https://github.com/lithic-com/lithic-python/compare/v0.33.0...v0.34.0)

### Features

* **api:** add `account_token` and `card_program_token` to `Card` ([#347](https://github.com/lithic-com/lithic-python/issues/347)) ([f94944e](https://github.com/lithic-com/lithic-python/commit/f94944e70f2666fd7a57cd8546146931242e78db))

## 0.33.0 (2024-01-31)

Full Changelog: [v0.32.0...v0.33.0](https://github.com/lithic-com/lithic-python/compare/v0.32.0...v0.33.0)

### Features

* **api:** add search_by_pan endpoint ([#342](https://github.com/lithic-com/lithic-python/issues/342)) ([2eb8a3c](https://github.com/lithic-com/lithic-python/commit/2eb8a3c4e573a9c9f71ba6ae7a3ab32e63ee0150))
* **client:** enable follow redirects by default ([#338](https://github.com/lithic-com/lithic-python/issues/338)) ([ec5cddd](https://github.com/lithic-com/lithic-python/commit/ec5cddd8419944fd3bc796232428bb08ab751bef))
* **client:** support parsing custom response types ([#343](https://github.com/lithic-com/lithic-python/issues/343)) ([ac44618](https://github.com/lithic-com/lithic-python/commit/ac44618a38700b84c95d2cd0c954e5211901a4e7))
* remove idempotency headers ([#346](https://github.com/lithic-com/lithic-python/issues/346)) ([79049f4](https://github.com/lithic-com/lithic-python/commit/79049f4b235f7e3d23f997f14030b818e69a54b8))


### Chores

* **internal:** cast type in mocked test ([#344](https://github.com/lithic-com/lithic-python/issues/344)) ([aa6e754](https://github.com/lithic-com/lithic-python/commit/aa6e75451bb9cbd667a2a6f1d02f2aa741079751))
* **internal:** enable ruff type checking misuse lint rule ([#341](https://github.com/lithic-com/lithic-python/issues/341)) ([312383f](https://github.com/lithic-com/lithic-python/commit/312383fc2a5a3a0719b795e38093d47d831fa486))
* **internal:** support multipart data with overlapping keys ([#340](https://github.com/lithic-com/lithic-python/issues/340)) ([e74deea](https://github.com/lithic-com/lithic-python/commit/e74deea8e769d38d147d8581fb238fb179b6ca0d))
* **internal:** support pre-release versioning ([#345](https://github.com/lithic-com/lithic-python/issues/345)) ([44505cc](https://github.com/lithic-com/lithic-python/commit/44505cca7cf92abd80e75e917fb08dbd55369088))

## 0.32.0 (2024-01-23)

Full Changelog: [v0.31.1...v0.32.0](https://github.com/lithic-com/lithic-python/compare/v0.31.1...v0.32.0)

### ⚠ BREAKING CHANGES

* **api:** change account holder creation response, new settlement detail type ([#337](https://github.com/lithic-com/lithic-python/issues/337))

### Features

* **api:** change account holder creation response, new settlement detail type ([#337](https://github.com/lithic-com/lithic-python/issues/337)) ([6d8a046](https://github.com/lithic-com/lithic-python/commit/6d8a046f9b91e9f7ea92239440bb38174d2ca83c))


### Chores

* **ci:** rely on Stainless GitHub App for releases ([#334](https://github.com/lithic-com/lithic-python/issues/334)) ([90063d7](https://github.com/lithic-com/lithic-python/commit/90063d766e5946f6735edc412a184f624c6b0807))
* **internal:** add internal helpers ([#336](https://github.com/lithic-com/lithic-python/issues/336)) ([9849b51](https://github.com/lithic-com/lithic-python/commit/9849b51a40a4f9dcd963d27b2021b0d998fe1364))
* **internal:** remove redundant client test ([#331](https://github.com/lithic-com/lithic-python/issues/331)) ([18ad2ad](https://github.com/lithic-com/lithic-python/commit/18ad2ad63019d1cc4c48ecb87a64a579e8934dda))
* **internal:** share client instances between all tests ([#335](https://github.com/lithic-com/lithic-python/issues/335)) ([0fe132a](https://github.com/lithic-com/lithic-python/commit/0fe132a60276eb4a82bf40e70367b8aff2df6505))
* **internal:** speculative retry-after-ms support ([#332](https://github.com/lithic-com/lithic-python/issues/332)) ([579486a](https://github.com/lithic-com/lithic-python/commit/579486aa985ace86e1832e35dd9d6ac47067b79c))
* lazy load raw resource class properties ([#333](https://github.com/lithic-com/lithic-python/issues/333)) ([e275233](https://github.com/lithic-com/lithic-python/commit/e275233d607e7bbb311b536ec674be8bf4ce8ea8))

## 0.31.1 (2024-01-17)

Full Changelog: [v0.31.0...v0.31.1](https://github.com/lithic-com/lithic-python/compare/v0.31.0...v0.31.1)

### Features

* **api:** updates ([#329](https://github.com/lithic-com/lithic-python/issues/329)) ([df87083](https://github.com/lithic-com/lithic-python/commit/df870839f6beb7416faa626643bd8ede8b14730b))


### Chores

* add write_to_file binary helper method ([#327](https://github.com/lithic-com/lithic-python/issues/327)) ([86d0a5c](https://github.com/lithic-com/lithic-python/commit/86d0a5c7279d67902ba75d73a599bc08894c016a))
* **internal:** fix typing util function ([#328](https://github.com/lithic-com/lithic-python/issues/328)) ([40c5279](https://github.com/lithic-com/lithic-python/commit/40c52799f31fae46d99580a5f19c9aa0366cbb88))
* **internal:** updates to proxy helper ([#325](https://github.com/lithic-com/lithic-python/issues/325)) ([9439dcc](https://github.com/lithic-com/lithic-python/commit/9439dcc885ba87841c6197beb005bde1deb22dad))

## 0.31.0 (2024-01-16)

Full Changelog: [v0.30.0...v0.31.0](https://github.com/lithic-com/lithic-python/compare/v0.30.0...v0.31.0)

### Features

* **client:** add support for streaming raw responses ([#323](https://github.com/lithic-com/lithic-python/issues/323)) ([ab894d3](https://github.com/lithic-com/lithic-python/commit/ab894d33ad10b3499150d5e6ecd9fb58fbeb03ea))


### Bug Fixes

* **client:** ensure path params are non-empty ([#324](https://github.com/lithic-com/lithic-python/issues/324)) ([c569801](https://github.com/lithic-com/lithic-python/commit/c5698014d94eef9733395a67c7cf380ecc5874f6))


### Chores

* **client:** improve debug logging for failed requests ([#320](https://github.com/lithic-com/lithic-python/issues/320)) ([c68b9a6](https://github.com/lithic-com/lithic-python/commit/c68b9a68027f178beb1bde1cae3d69a34ae9100a))


### Documentation

* **readme:** improve api reference ([#322](https://github.com/lithic-com/lithic-python/issues/322)) ([fcac257](https://github.com/lithic-com/lithic-python/commit/fcac257751b887ddcbae7c6b0d30f76291892277))

## 0.30.0 (2024-01-09)

Full Changelog: [v0.29.1...v0.30.0](https://github.com/lithic-com/lithic-python/compare/v0.29.1...v0.30.0)

### Features

* add `None` default value to nullable response properties ([#315](https://github.com/lithic-com/lithic-python/issues/315)) ([81458b1](https://github.com/lithic-com/lithic-python/commit/81458b1cf5c7d260509b1606d1e21e9b8c9d495f))
* **api:** add card renew endpoint ([#319](https://github.com/lithic-com/lithic-python/issues/319)) ([2ec8b25](https://github.com/lithic-com/lithic-python/commit/2ec8b251e6f7e8969a9fca78563eca07bd899444))


### Chores

* add .keep files for examples and custom code directories ([#318](https://github.com/lithic-com/lithic-python/issues/318)) ([d21bb0c](https://github.com/lithic-com/lithic-python/commit/d21bb0c1753d546491c04dadd0e77049c0def489))
* **internal:** bump license ([#312](https://github.com/lithic-com/lithic-python/issues/312)) ([03038ed](https://github.com/lithic-com/lithic-python/commit/03038ed1dec2cd2407eb34a4c05b5c7d84390b16))
* **internal:** loosen type var restrictions ([#317](https://github.com/lithic-com/lithic-python/issues/317)) ([fae02b2](https://github.com/lithic-com/lithic-python/commit/fae02b2eb95f8a8e26a7e651cdd76292c1d6879f))
* **internal:** replace isort with ruff ([#314](https://github.com/lithic-com/lithic-python/issues/314)) ([8b841b0](https://github.com/lithic-com/lithic-python/commit/8b841b00f186701c9b6e101dd7e2500cafd7dfc1))
* use property declarations for resource members ([#316](https://github.com/lithic-com/lithic-python/issues/316)) ([969451f](https://github.com/lithic-com/lithic-python/commit/969451f761be877fee3dc2b388154f15198185b6))

## 0.29.1 (2023-12-28)

Full Changelog: [v0.29.0...v0.29.1](https://github.com/lithic-com/lithic-python/compare/v0.29.0...v0.29.1)

### Bug Fixes

* **client:** correctly use custom http client auth ([#311](https://github.com/lithic-com/lithic-python/issues/311)) ([d3913db](https://github.com/lithic-com/lithic-python/commit/d3913dbd6bc3cd7516309eb0461a78903e893cdb))


### Chores

* **internal:** add bin script ([#308](https://github.com/lithic-com/lithic-python/issues/308)) ([1d9b46f](https://github.com/lithic-com/lithic-python/commit/1d9b46f318723f2d37f6b263eaf234f2f3a05352))
* **internal:** fix typos ([#306](https://github.com/lithic-com/lithic-python/issues/306)) ([e8c2919](https://github.com/lithic-com/lithic-python/commit/e8c29193c1ff29ae3517f80bbe3290b1a4f19323))
* **internal:** minor utils restructuring ([#305](https://github.com/lithic-com/lithic-python/issues/305)) ([9c1c54d](https://github.com/lithic-com/lithic-python/commit/9c1c54d8112838c46e360251f5c7de8c7bca5e58))
* **internal:** updates to base client ([#303](https://github.com/lithic-com/lithic-python/issues/303)) ([ab29f31](https://github.com/lithic-com/lithic-python/commit/ab29f3175f825fb5625e372a2b49516bd92b46f8))
* **internal:** use ruff instead of black for formatting ([#310](https://github.com/lithic-com/lithic-python/issues/310)) ([87c7468](https://github.com/lithic-com/lithic-python/commit/87c7468555a6070bf2c1b729ea68a68139203a96))
* **package:** bump minimum typing-extensions to 4.7 ([#307](https://github.com/lithic-com/lithic-python/issues/307)) ([ef333f2](https://github.com/lithic-com/lithic-python/commit/ef333f2f23c8b685a73e9914253a3bff8e3d9a43))

## 0.29.0 (2023-12-18)

Full Changelog: [v0.28.0...v0.29.0](https://github.com/lithic-com/lithic-python/compare/v0.28.0...v0.29.0)

### Features

* **api:** remove /auth_stream enrollment endpoints ([#302](https://github.com/lithic-com/lithic-python/issues/302)) ([a810e9c](https://github.com/lithic-com/lithic-python/commit/a810e9c432ca762a3d9fa9b10f8ce790ebbcef53))


### Chores

* **ci:** run release workflow once per day ([#300](https://github.com/lithic-com/lithic-python/issues/300)) ([edfd745](https://github.com/lithic-com/lithic-python/commit/edfd745018f2e823ec654a00aaacdfd78475f43e))

## 0.28.0 (2023-12-15)

Full Changelog: [v0.27.2...v0.28.0](https://github.com/lithic-com/lithic-python/compare/v0.27.2...v0.28.0)

### Features

* **api:** rename `token` and `type` to `financial_account_token` and `financial_account_type` ([#299](https://github.com/lithic-com/lithic-python/issues/299)) ([e7fe65c](https://github.com/lithic-com/lithic-python/commit/e7fe65c5fed56e356d54d2a6dcb1e6140f3dcd5e))


### Documentation

* improve README timeout comment ([#295](https://github.com/lithic-com/lithic-python/issues/295)) ([fe21964](https://github.com/lithic-com/lithic-python/commit/fe2196458b282980d86dfefc9a68a05717397f33))


### Refactors

* **client:** simplify cleanup ([#297](https://github.com/lithic-com/lithic-python/issues/297)) ([226aea9](https://github.com/lithic-com/lithic-python/commit/226aea9169cf26d3ef7c6bd7f23d318fb7069332))
* simplify internal error handling ([#298](https://github.com/lithic-com/lithic-python/issues/298)) ([95aa1a1](https://github.com/lithic-com/lithic-python/commit/95aa1a190b994d6ec6e893975430adbda6b8bfd0))

## 0.27.2 (2023-12-08)

Full Changelog: [v0.27.1...v0.27.2](https://github.com/lithic-com/lithic-python/compare/v0.27.1...v0.27.2)

### Bug Fixes

* avoid leaking memory when Client.with_options is used ([#293](https://github.com/lithic-com/lithic-python/issues/293)) ([7d31816](https://github.com/lithic-com/lithic-python/commit/7d318161f5d7795fda3bd12ed86075e6f5bb4fdf))

## 0.27.1 (2023-12-08)

Full Changelog: [v0.27.0...v0.27.1](https://github.com/lithic-com/lithic-python/compare/v0.27.0...v0.27.1)

### Bug Fixes

* **errors:** properly assign APIError.body ([#292](https://github.com/lithic-com/lithic-python/issues/292)) ([b331f3a](https://github.com/lithic-com/lithic-python/commit/b331f3a80f2fdfa23150cabb1c6ebf8ebbd056a1))


### Chores

* **internal:** enable more lint rules ([#291](https://github.com/lithic-com/lithic-python/issues/291)) ([81d6f42](https://github.com/lithic-com/lithic-python/commit/81d6f4263dc7c80c82ab258c09980c55d659dd7c))
* **internal:** minor updates to pagination ([#289](https://github.com/lithic-com/lithic-python/issues/289)) ([c47d429](https://github.com/lithic-com/lithic-python/commit/c47d429e5aad580749d6e1feaf5a499128ae4244))
* **internal:** reformat imports ([#287](https://github.com/lithic-com/lithic-python/issues/287)) ([1129916](https://github.com/lithic-com/lithic-python/commit/112991699bf979352d62304ed25d15242e766867))
* **internal:** reformat imports ([#290](https://github.com/lithic-com/lithic-python/issues/290)) ([78d4f94](https://github.com/lithic-com/lithic-python/commit/78d4f9460aa5d5f1a798606d9a604c6faa887d88))
* **internal:** update formatting ([#288](https://github.com/lithic-com/lithic-python/issues/288)) ([5551a3d](https://github.com/lithic-com/lithic-python/commit/5551a3d01b7a8f2156bb0c6298d7d684e0697b6c))

## 0.27.0 (2023-12-05)

Full Changelog: [v0.26.2...v0.27.0](https://github.com/lithic-com/lithic-python/compare/v0.26.2...v0.27.0)

### Features

* **api:** remove `CLOSED` account enum and update docstrings ([#284](https://github.com/lithic-com/lithic-python/issues/284)) ([6441b1e](https://github.com/lithic-com/lithic-python/commit/6441b1e84499de12ab8061435c8fb19433080791))


### Chores

* **package:** lift anyio v4 restriction ([#281](https://github.com/lithic-com/lithic-python/issues/281)) ([ce7e5df](https://github.com/lithic-com/lithic-python/commit/ce7e5dff5f2b5a7421e339f56e247aca8c6ce77e))

## 0.26.2 (2023-12-01)

Full Changelog: [v0.26.1...v0.26.2](https://github.com/lithic-com/lithic-python/compare/v0.26.1...v0.26.2)

### Bug Fixes

* **client:** correct base_url setter implementation ([#280](https://github.com/lithic-com/lithic-python/issues/280)) ([1b9427c](https://github.com/lithic-com/lithic-python/commit/1b9427c63f66436546acc3d2e364b934f38b369e))


### Chores

* **internal:** minor internal restructuring ([#277](https://github.com/lithic-com/lithic-python/issues/277)) ([c897da5](https://github.com/lithic-com/lithic-python/commit/c897da57f18fe3c2dcd069d3419600d2971ae145))
* **internal:** remove unused type var ([#279](https://github.com/lithic-com/lithic-python/issues/279)) ([fcdcf4b](https://github.com/lithic-com/lithic-python/commit/fcdcf4bbaf0d87ea0017a77254f0971009e4162b))
* **internal:** replace string concatenation with f-strings ([#278](https://github.com/lithic-com/lithic-python/issues/278)) ([b6d02a1](https://github.com/lithic-com/lithic-python/commit/b6d02a19a2cbc9c431bdd93f2e99c14f9692c5fd))


### Documentation

* **readme:** update example snippets ([#275](https://github.com/lithic-com/lithic-python/issues/275)) ([83f9eb1](https://github.com/lithic-com/lithic-python/commit/83f9eb180314f1a03f620774723e5f614d7cd89d))

## 0.26.1 (2023-11-30)

Full Changelog: [v0.26.0...v0.26.1](https://github.com/lithic-com/lithic-python/compare/v0.26.0...v0.26.1)

### Bug Fixes

* **client:** ensure retried requests are closed ([#274](https://github.com/lithic-com/lithic-python/issues/274)) ([2275961](https://github.com/lithic-com/lithic-python/commit/227596193414b5d5bb808a7a46a63eb87b1f22fe))


### Chores

* **internal:** add tests for proxy change ([#273](https://github.com/lithic-com/lithic-python/issues/273)) ([9d30cdd](https://github.com/lithic-com/lithic-python/commit/9d30cdd88beb4de82f0a9b47d834a13443be19c0))
* **internal:** minor pagination updates ([#270](https://github.com/lithic-com/lithic-python/issues/270)) ([4affab9](https://github.com/lithic-com/lithic-python/commit/4affab9c62b29a8ae4a2aa427e1d4a162e80fed7))
* **internal:** updates to proxy helper ([#272](https://github.com/lithic-com/lithic-python/issues/272)) ([5dc86c8](https://github.com/lithic-com/lithic-python/commit/5dc86c88f75e1f18a3510d97ba99cf9218283d10))

## 0.26.0 (2023-11-28)

Full Changelog: [v0.25.1...v0.26.0](https://github.com/lithic-com/lithic-python/compare/v0.25.1...v0.26.0)

### Features

* **api:** add `get spend_limits` endpoints to `cards` and `accounts` ([#269](https://github.com/lithic-com/lithic-python/issues/269)) ([d5601a3](https://github.com/lithic-com/lithic-python/commit/d5601a38388dba4f014d6e49efaf405e3ea297bb))


### Chores

* **client:** improve copy method ([#262](https://github.com/lithic-com/lithic-python/issues/262)) ([aac41f4](https://github.com/lithic-com/lithic-python/commit/aac41f49d9123f1ebc51e15f97511784cd159634))
* **deps:** bump mypy to v1.7.1 ([#268](https://github.com/lithic-com/lithic-python/issues/268)) ([70c9557](https://github.com/lithic-com/lithic-python/commit/70c9557bb8691e8e7ce46ae2e1ba549502bbc00f))
* **internal:** options updates ([#265](https://github.com/lithic-com/lithic-python/issues/265)) ([a691ce0](https://github.com/lithic-com/lithic-python/commit/a691ce07ca025e02aca60b14058fbcd66ac18a28))
* **internal:** revert recent options change ([#266](https://github.com/lithic-com/lithic-python/issues/266)) ([3068340](https://github.com/lithic-com/lithic-python/commit/30683402609944684fac80f9dd9275e0edc5d4be))
* **internal:** send more detailed x-stainless headers ([#267](https://github.com/lithic-com/lithic-python/issues/267)) ([685ae57](https://github.com/lithic-com/lithic-python/commit/685ae5742a7afe6cb2d29080366b3050e7d459f1))
* **package:** add license classifier metadata ([#264](https://github.com/lithic-com/lithic-python/issues/264)) ([9a66cfd](https://github.com/lithic-com/lithic-python/commit/9a66cfdecce8374e8d25fd16ba5f5c39081bafbc))

## 0.25.1 (2023-11-21)

Full Changelog: [v0.25.0...v0.25.1](https://github.com/lithic-com/lithic-python/compare/v0.25.0...v0.25.1)

### Bug Fixes

* **client:** attempt to parse unknown json content types ([#261](https://github.com/lithic-com/lithic-python/issues/261)) ([e8650d3](https://github.com/lithic-com/lithic-python/commit/e8650d31ee68cc5450def70a8565b7c286a6a6b4))


### Chores

* **internal:** update stats file ([#259](https://github.com/lithic-com/lithic-python/issues/259)) ([f312176](https://github.com/lithic-com/lithic-python/commit/f3121762d0fdd18bba8bbb214fac6a354a22ae36))
* **internal:** update type hint for helper function ([#260](https://github.com/lithic-com/lithic-python/issues/260)) ([ee16cd4](https://github.com/lithic-com/lithic-python/commit/ee16cd4f41dbee183b7e490321f434d332d185c2))


### Documentation

* **readme:** minor updates ([#257](https://github.com/lithic-com/lithic-python/issues/257)) ([f20d860](https://github.com/lithic-com/lithic-python/commit/f20d860ad1ae935e3428ee4e1dfdef5128aa6e70))

## 0.25.0 (2023-11-16)

Full Changelog: [v0.24.3...v0.25.0](https://github.com/lithic-com/lithic-python/compare/v0.24.3...v0.25.0)

### Features

* **api:** updates ([#256](https://github.com/lithic-com/lithic-python/issues/256)) ([fd10ea1](https://github.com/lithic-com/lithic-python/commit/fd10ea17206bb1a329aba07bc21a0d4472013678))
* **client:** support reading the base url from an env variable ([#255](https://github.com/lithic-com/lithic-python/issues/255)) ([6f74bc5](https://github.com/lithic-com/lithic-python/commit/6f74bc5dc7cb8660913ff9612ed441158522904e))


### Chores

* **internal:** fix devcontainer interpeter path ([#253](https://github.com/lithic-com/lithic-python/issues/253)) ([17d39da](https://github.com/lithic-com/lithic-python/commit/17d39da204bc473fca803232f6942e879b4d6dc8))
* **internal:** fix typo in NotGiven docstring ([#251](https://github.com/lithic-com/lithic-python/issues/251)) ([be151c6](https://github.com/lithic-com/lithic-python/commit/be151c69e40b2dc13c7b6086dad4bbab3c8d7342))


### Documentation

* fix code comment typo ([#254](https://github.com/lithic-com/lithic-python/issues/254)) ([9437ea3](https://github.com/lithic-com/lithic-python/commit/9437ea3fcba7ba23a50852e1d1a0f119b1636680))

## 0.24.3 (2023-11-13)

Full Changelog: [v0.24.2...v0.24.3](https://github.com/lithic-com/lithic-python/compare/v0.24.2...v0.24.3)

### Bug Fixes

* **client:** retry if SSLWantReadError occurs in the async client ([#249](https://github.com/lithic-com/lithic-python/issues/249)) ([1267620](https://github.com/lithic-com/lithic-python/commit/1267620391bf4dd7358a767ca0944156f05fea72))

## 0.24.2 (2023-11-10)

Full Changelog: [v0.24.1...v0.24.2](https://github.com/lithic-com/lithic-python/compare/v0.24.1...v0.24.2)

### Bug Fixes

* **client:** serialise pydantic v1 default fields correctly in params ([#247](https://github.com/lithic-com/lithic-python/issues/247)) ([ed6f61a](https://github.com/lithic-com/lithic-python/commit/ed6f61a910bd4511967b97ed70b588368530ef8b))

## 0.24.1 (2023-11-10)

Full Changelog: [v0.24.0...v0.24.1](https://github.com/lithic-com/lithic-python/compare/v0.24.0...v0.24.1)

### Bug Fixes

* **models:** mark unknown fields as set in pydantic v1 ([#246](https://github.com/lithic-com/lithic-python/issues/246)) ([a495004](https://github.com/lithic-com/lithic-python/commit/a495004cc3d994860aa40a4adf6d1d4542f4be36))


### Chores

* **internal:** base client updates ([#245](https://github.com/lithic-com/lithic-python/issues/245)) ([f29d219](https://github.com/lithic-com/lithic-python/commit/f29d219dbb4c89d61820e84e1e059820e25085a7))


### Documentation

* reword package description ([#243](https://github.com/lithic-com/lithic-python/issues/243)) ([44e8d9f](https://github.com/lithic-com/lithic-python/commit/44e8d9fec40a837edacc9d2bdd741b0a5671b07b))

## 0.24.0 (2023-11-09)

Full Changelog: [v0.23.0...v0.24.0](https://github.com/lithic-com/lithic-python/compare/v0.23.0...v0.24.0)

### Features

* **api:** updates ([#242](https://github.com/lithic-com/lithic-python/issues/242)) ([eecfe4d](https://github.com/lithic-com/lithic-python/commit/eecfe4df66172f4cf4b55c46d9032d7a923c802e))
* **client:** support passing chunk size for binary responses ([#241](https://github.com/lithic-com/lithic-python/issues/241)) ([9bbaf15](https://github.com/lithic-com/lithic-python/commit/9bbaf15763aadce9de1993e1b786c77e98584f99))


### Chores

* **internal:** improve github devcontainer setup ([#239](https://github.com/lithic-com/lithic-python/issues/239)) ([c95e537](https://github.com/lithic-com/lithic-python/commit/c95e5374ff981d8249b77bfc2d1476eb1181d278))

## 0.23.0 (2023-11-08)

Full Changelog: [v0.22.2...v0.23.0](https://github.com/lithic-com/lithic-python/compare/v0.22.2...v0.23.0)

### Features

* **client:** support passing httpx.Timeout to method timeout argument ([#234](https://github.com/lithic-com/lithic-python/issues/234)) ([d70cab3](https://github.com/lithic-com/lithic-python/commit/d70cab37a0ef4a4cb76bce9ceb27a0591de65044))


### Bug Fixes

* **api:** correct type for other fees details ([#238](https://github.com/lithic-com/lithic-python/issues/238)) ([3e4efea](https://github.com/lithic-com/lithic-python/commit/3e4efea1d64c2dd51e9884dc7fd270d851424d41))


### Chores

* **docs:** fix github links ([#237](https://github.com/lithic-com/lithic-python/issues/237)) ([d747b8c](https://github.com/lithic-com/lithic-python/commit/d747b8c91d76843003394ccadca00f191fc19f81))
* **internal:** fix some typos ([#236](https://github.com/lithic-com/lithic-python/issues/236)) ([ac40586](https://github.com/lithic-com/lithic-python/commit/ac4058660e21d2a5248fb4f354854be495f533ee))

## 0.22.2 (2023-11-06)

Full Changelog: [v0.22.1...v0.22.2](https://github.com/lithic-com/lithic-python/compare/v0.22.1...v0.22.2)

### Bug Fixes

* prevent TypeError in Python 3.8 (ABC is not subscriptable) ([#233](https://github.com/lithic-com/lithic-python/issues/233)) ([55fd8a3](https://github.com/lithic-com/lithic-python/commit/55fd8a3315c546a4c83ff8e72b36aff78d7c7209))


### Chores

* **internal:** remove unused int/float conversion ([#231](https://github.com/lithic-com/lithic-python/issues/231)) ([1256055](https://github.com/lithic-com/lithic-python/commit/125605517acc43343c15a382c10ce535304c22d6))


### Documentation

* **api:** improve method signatures for named path params ([#228](https://github.com/lithic-com/lithic-python/issues/228)) ([476d296](https://github.com/lithic-com/lithic-python/commit/476d2960e890068e851c4d443533704178912431))
* improve account holder control person documentation ([#230](https://github.com/lithic-com/lithic-python/issues/230)) ([36abfb0](https://github.com/lithic-com/lithic-python/commit/36abfb09f32eb367c6f4bba24c737bcf585defea))
* **readme:** improve example snippets ([#232](https://github.com/lithic-com/lithic-python/issues/232)) ([ace36a4](https://github.com/lithic-com/lithic-python/commit/ace36a44b8f7fc05ebec0842d6be702150a71a3c))

## 0.22.1 (2023-11-03)

Full Changelog: [v0.22.0...v0.22.1](https://github.com/lithic-com/lithic-python/compare/v0.22.0...v0.22.1)

### Bug Fixes

* **binaries:** don't synchronously block in astream_to_file ([#226](https://github.com/lithic-com/lithic-python/issues/226)) ([cfc5441](https://github.com/lithic-com/lithic-python/commit/cfc5441a47342e6ea57683222b15836404c0d50b))

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
