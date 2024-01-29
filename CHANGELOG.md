# Changelog

## [3.0.0](https://github.com/threatcode/pyattck-data/compare/v2.6.3...3.0.0) (2024-01-29)


### ⚠ BREAKING CHANGES

* Adding splunk security content to dataset.

### Features

* Added last_updated field to MitreAttck data model ([ffc31c6](https://github.com/threatcode/pyattck-data/commit/ffc31c65d322b4ea326d1f851bce7172a853bd3d))
* Adding nist_controls json to generation code ([d921d66](https://github.com/threatcode/pyattck-data/commit/d921d669053e129f67fbf2b3434025dcb5a3f100))
* Adding print statement when data arguments have changed or do not match data models ([7e6ffec](https://github.com/threatcode/pyattck-data/commit/7e6ffec8c16a9255a5c6d0bc42a13412f38589ba))
* Adding splunk security content to dataset. ([ea7b52f](https://github.com/threatcode/pyattck-data/commit/ea7b52f3e92621b18607cf8952022c7f0bcf5a94))
* Adding technique_id and stix properties for convenience ([515d4b0](https://github.com/threatcode/pyattck-data/commit/515d4b0940e73919adb7e2059a62e9332744b068))
* bumping minor version ([591d644](https://github.com/threatcode/pyattck-data/commit/591d6449c9afa9ffffd3e88c907a527ede47015f))
* Split generation of data to it's own pacakge ([0b98775](https://github.com/threatcode/pyattck-data/commit/0b98775b264d7eb40d8dcefabba87b9e2fefda1b))
* Splitting pyattck_data and generation of external data ([dcf463b](https://github.com/threatcode/pyattck-data/commit/dcf463b7d316bf807b2aa4cd7790cb45c80eaa67))
* Updated to new data models ([78d5856](https://github.com/threatcode/pyattck-data/commit/78d5856947f4d20af8417e9f78eb805240bc35b0))
* Updating CI ([06db38b](https://github.com/threatcode/pyattck-data/commit/06db38b4f7d7dfca3b6b06a830804f18d8562b2a))
* Updating version and codecov percentage ([f707663](https://github.com/threatcode/pyattck-data/commit/f707663e19e6d96db2cfc1bd51039902a67ce79a))


### Bug Fixes

* **actor:** Updated init and post_init in model ([6883342](https://github.com/threatcode/pyattck-data/commit/68833429b36f90f0a9dfc764ccc8522ac6e5ce2f))
* **actor:** Updated init and post_init in model ([ac5487b](https://github.com/threatcode/pyattck-data/commit/ac5487bf249f05ca1f0ce1e25feb8da4a754e246))
* **actor:** Updated init in model ([c9f49db](https://github.com/threatcode/pyattck-data/commit/c9f49db8d098d4ff5748ed9449071ab259f95987))
* Adding better logic to filter out multiple tactics ([7769690](https://github.com/threatcode/pyattck-data/commit/7769690f9d11747b86d4807eb44b9b030f826bf5))
* Adding campaigns entities as properties to malwar, techniques and tools ([d5a4dc5](https://github.com/threatcode/pyattck-data/commit/d5a4dc55ced2a04c3d0084180819eb0a58ce2dab))
* **attack:** Updated init in model ([51fb2be](https://github.com/threatcode/pyattck-data/commit/51fb2beecc3969dcb7ae149611f93e00eb6d0b74))
* Bump patch version ([df60bad](https://github.com/threatcode/pyattck-data/commit/df60bad3a7813c1648a9b7d28dd2870f038d27fb))
* Bumped and updated dependencies ([cdc98c2](https://github.com/threatcode/pyattck-data/commit/cdc98c27e4c91962b77dd983348b71b4dffb7bfc))
* Bumped patch version ([ef42df3](https://github.com/threatcode/pyattck-data/commit/ef42df3fbf2e7bb8321b1f9e626c8bae52c39ef6))
* **control:** Updated init in model ([8fb77a7](https://github.com/threatcode/pyattck-data/commit/8fb77a751e4be217258f1c76d06895d72a28c22c))
* Data file updates ([03b2535](https://github.com/threatcode/pyattck-data/commit/03b2535f51bbe0f4d42a17f55c5a6463c3aebb9e))
* **datacomponent:** Updated init in model ([5eff4b0](https://github.com/threatcode/pyattck-data/commit/5eff4b0959f16837c9e8c8f9eccc09d3de8f9917))
* **datasource:** Updated init in model ([81bbcd2](https://github.com/threatcode/pyattck-data/commit/81bbcd232304a96ea99973295333b99048cd6e19))
* **definition:** Updated init, post init and added revoked in model ([07d46bf](https://github.com/threatcode/pyattck-data/commit/07d46bfdca790aab4c30d9778c205ec03a793813))
* Ensuring tactic objects are unique. Fixes [#124](https://github.com/threatcode/pyattck-data/issues/124) ([f5da605](https://github.com/threatcode/pyattck-data/commit/f5da6052165f43819d095fd75cf58d49f7b520d5))
* Fixing [#62](https://github.com/threatcode/pyattck-data/issues/62) by removing googletrans and replacing with deep-translate. Also moving some dependencies to only be installed via CI since that is where they are exclusively used. ([d32b0de](https://github.com/threatcode/pyattck-data/commit/d32b0defcaf14b07a8d6b3904c4fa7af3b815b9e))
* **generated:** Updated post_init in model ([df47c5f](https://github.com/threatcode/pyattck-data/commit/df47c5fd7cd9725cb4fa74ef5547d0e9c7c7a57e))
* **malware:** Updated init in model ([2f65f5e](https://github.com/threatcode/pyattck-data/commit/2f65f5ee0949c03cd06efedcdace49a20b5ae76e))
* **matrix:** Added revoked property in matrix ([e5d75f3](https://github.com/threatcode/pyattck-data/commit/e5d75f3a6a4f044661b1ce14d2863fbd0ac0a391))
* Minor deps updates ([9d268f5](https://github.com/threatcode/pyattck-data/commit/9d268f5556a1f0dc5915ba704e065474f674ca69))
* **mitigation:** Updated init in model ([221c0c9](https://github.com/threatcode/pyattck-data/commit/221c0c940df6e9d9e6f02c2f728d5b2715cd1c9a))
* **nist:** Updated post_init in model ([95cfc29](https://github.com/threatcode/pyattck-data/commit/95cfc29498cadbbe9385301e6db77c5c91e83966))
* **relationship:** Updated init and post_init in model ([927455e](https://github.com/threatcode/pyattck-data/commit/927455e37fa2b8c57de799341b3fb4c919480e88))
* Removing markdown dependency ([6ce15e8](https://github.com/threatcode/pyattck-data/commit/6ce15e8bffe693406762d3fe0dc9caeb23c364db))
* Replaced googletrans with deep-translator in Threathunting Playbook ([cd43a90](https://github.com/threatcode/pyattck-data/commit/cd43a90a8b9d432d902c6326de73161fbb8ca304))
* **tactics:** Updated how we retrieve tactics for techniques ([b70166c](https://github.com/threatcode/pyattck-data/commit/b70166c5e5ed880c95596df7390e07fa8f1c37ae))
* **tactic:** Updated init in model ([e56add7](https://github.com/threatcode/pyattck-data/commit/e56add7f3e213f348e26b7d6b5195aac07dadff2))
* **technique:** Updated init and post_init in model ([6f1470e](https://github.com/threatcode/pyattck-data/commit/6f1470e405d14fa8bf2ff10e17ca917521fd1d7f))
* **tool:** Updated init in model ([3bd310d](https://github.com/threatcode/pyattck-data/commit/3bd310d215776387ad45fd687327b541f7b8f901))
* Update patch version ([a015cad](https://github.com/threatcode/pyattck-data/commit/a015cada8d989c33daa9d658e1187e2e87356bad))
* Updated docs ([d7de215](https://github.com/threatcode/pyattck-data/commit/d7de21548e25bc9bb89558f663fa05258b3e9285))
* Updated last_updated timestamp ([e8816d4](https://github.com/threatcode/pyattck-data/commit/e8816d43800d2a6efb1a991267546af751546503))
* Updated malware arch generated data collection ([f128ba4](https://github.com/threatcode/pyattck-data/commit/f128ba4b01dd49561ecfe264fa6d204a5806562e))
* Updated minor version ([b5a4ac3](https://github.com/threatcode/pyattck-data/commit/b5a4ac3707eea41417006d31fe4e1d5f2108c1de))
* Updated patch version ([a7d260a](https://github.com/threatcode/pyattck-data/commit/a7d260a312707990c459aead225f9e8d63585d55))
* Updating actor comment field to comments list field ([afc5b18](https://github.com/threatcode/pyattck-data/commit/afc5b183d5f1f46e3d9ed4cd3d1a9379ca512fdf))
* Updating adversary emulation data generation ([7eb2a59](https://github.com/threatcode/pyattck-data/commit/7eb2a59daf0e278fc053f4c5a396780ce5eed5f9))
* Updating attackempire generation ([6f6d03f](https://github.com/threatcode/pyattck-data/commit/6f6d03f539c59c98d6cc3382f7e9bbdd78de1aa3))
* Updating error handling and checking in generated data ([ddd8fbf](https://github.com/threatcode/pyattck-data/commit/ddd8fbf7691a9507feb8558a0d9d9a25f64e2b6c))
* Updating importlib-metadata dependency ([f11d10b](https://github.com/threatcode/pyattck-data/commit/f11d10b09acf61a39d2293a36f3a444b2db263be))
* Updating minor version ([3c8c586](https://github.com/threatcode/pyattck-data/commit/3c8c586655613b10331199a4f4a3c94a43b76cf8))
* Updating pip version ([c7e5c12](https://github.com/threatcode/pyattck-data/commit/c7e5c129a743f51a43f1ca62ec065b1c6584f16c))
* Updating to external_tools propertyy in add_actor_item method ([7d2517b](https://github.com/threatcode/pyattck-data/commit/7d2517b7a560d0d8598db6dc1a8fdb3e480d4ae8))
* Updating to support changes from Attack 13 ([d7cff7b](https://github.com/threatcode/pyattck-data/commit/d7cff7b64aa65351a8371b392800ec953e021c87))
* Updating version string in workflow ([bed3156](https://github.com/threatcode/pyattck-data/commit/bed31561241483e08ec46a985a2f2dc6bfa2490c))
* Updating version to 2.3.0 ([1d3b511](https://github.com/threatcode/pyattck-data/commit/1d3b51127b9f5b6a9684d5c0ef20c9750db3e65e))
* Upgrading dependencies ([8d2c9d5](https://github.com/threatcode/pyattck-data/commit/8d2c9d5556fdc621193bf8e3b4c88b943686a593))


### Documentation

* Updated requirements ([fd3a629](https://github.com/threatcode/pyattck-data/commit/fd3a62969df7aa8961fada9550ec3bb633373f32))

## [2.6.3](https://github.com/swimlane/pyattck-data/compare/2.6.2...2.6.3) (2023-05-11)


### Bug Fixes

* Updating error handling and checking in generated data ([ddd8fbf](https://github.com/swimlane/pyattck-data/commit/ddd8fbf7691a9507feb8558a0d9d9a25f64e2b6c))
* Updating to support changes from Attack 13 ([d7cff7b](https://github.com/swimlane/pyattck-data/commit/d7cff7b64aa65351a8371b392800ec953e021c87))

## [2.6.2](https://github.com/swimlane/pyattck-data/compare/2.6.1...2.6.2) (2023-02-10)


### Bug Fixes

* Updated docs ([d7de215](https://github.com/swimlane/pyattck-data/commit/d7de21548e25bc9bb89558f663fa05258b3e9285))

## [2.6.1](https://github.com/swimlane/pyattck-data/compare/v2.6.0...2.6.1) (2023-02-10)


### Bug Fixes

* Adding better logic to filter out multiple tactics ([7769690](https://github.com/swimlane/pyattck-data/commit/7769690f9d11747b86d4807eb44b9b030f826bf5))
* Adding campaigns entities as properties to malwar, techniques and tools ([d5a4dc5](https://github.com/swimlane/pyattck-data/commit/d5a4dc55ced2a04c3d0084180819eb0a58ce2dab))
* Ensuring tactic objects are unique. Fixes [#124](https://github.com/swimlane/pyattck-data/issues/124) ([f5da605](https://github.com/swimlane/pyattck-data/commit/f5da6052165f43819d095fd75cf58d49f7b520d5))
* Updating version string in workflow ([bed3156](https://github.com/swimlane/pyattck-data/commit/bed31561241483e08ec46a985a2f2dc6bfa2490c))
