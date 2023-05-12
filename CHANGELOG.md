# Changelog

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
