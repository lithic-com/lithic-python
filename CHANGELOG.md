# Changelog

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
