# Design-system repositories

The 36 owned IPs each have a dedicated public design-system repository under `ksamint`. Tiansight retains its existing repository. External reference IPs are excluded.

Each new repository starts with its tracked brand folder, published brand data, theme tokens, asset references, classification and source provenance. Source files keep their original paths. Binary media remains at its published URLs; already-tracked archives are preserved. No ignored local or private files were imported.

These are initial snapshots. Subsequent changes in a design-system repository do not automatically synchronize back to IPTrust. `config/brands.json` stores the catalog link in `designSystemUrl`.

| IP | Design-system repository |
| --- | --- |
| Table AI | [dsys_tableai](https://github.com/ksamint/dsys_tableai) |
| VANAHOM | [dsys_vanahom](https://github.com/ksamint/dsys_vanahom) |
| Sanctem | [dsys_sanctem](https://github.com/ksamint/dsys_sanctem) |
| KiND | [dsys_kind](https://github.com/ksamint/dsys_kind) |
| APHA | [dsys_apha](https://github.com/ksamint/dsys_apha) |
| MANA Endless | [dsys_manaendless](https://github.com/ksamint/dsys_manaendless) |
| OPC Global | [dsys_opcglobal](https://github.com/ksamint/dsys_opcglobal) |
| 岁知社 | [dsys_iptrust](https://github.com/ksamint/dsys_iptrust) |
| 峰值永造局 | [dsys_fengzhi](https://github.com/ksamint/dsys_fengzhi) |
| Axisee | [dsys_axisee](https://github.com/ksamint/dsys_axisee) |
| 侍天 - 智慧餐饮 | [dsys_tiansight01](https://github.com/ksamint/dsys_tiansight01) |
| 1stepmore | [dsys_1stepmore](https://github.com/ksamint/dsys_1stepmore) |
| AGEM | [dsys_agem](https://github.com/ksamint/dsys_agem) |
| RGD | [dsys_rgd](https://github.com/ksamint/dsys_rgd) |
| Changoods | [dsys_changoods](https://github.com/ksamint/dsys_changoods) |
| PKU BOYA Academy | [dsys_boya](https://github.com/ksamint/dsys_boya) |
| APUCH | [dsys_apuch](https://github.com/ksamint/dsys_apuch) |
| 帕姆建筑 | [dsys_pam](https://github.com/ksamint/dsys_pam) |
| ksamint | [dsys_ksamint](https://github.com/ksamint/dsys_ksamint) |
| iNucleus | [dsys_inucleus](https://github.com/ksamint/dsys_inucleus) |
| 信致旅游 | [dsys_xinzhi-travel](https://github.com/ksamint/dsys_xinzhi-travel) |
| 中智游集团 | [dsys_zhongzhiyou](https://github.com/ksamint/dsys_zhongzhiyou) |
| Nibiru | [dsys_nibiru](https://github.com/ksamint/dsys_nibiru) |
| 深圳微软出海中心 | [dsys_shenzhen-microsoft-global-center](https://github.com/ksamint/dsys_shenzhen-microsoft-global-center) |
| 山人境 | [dsys_shanrenjing](https://github.com/ksamint/dsys_shanrenjing) |
| 烤鱼神话 | [dsys_kaoyu-shenhua](https://github.com/ksamint/dsys_kaoyu-shenhua) |
| 延安石窑宾馆 | [dsys_yanan-shiyao-hotel](https://github.com/ksamint/dsys_yanan-shiyao-hotel) |
| 同里市集 | [dsys_tongli-market](https://github.com/ksamint/dsys_tongli-market) |
| 同香荟 | [dsys_tongxianghui](https://github.com/ksamint/dsys_tongxianghui) |
| 睦堂湾 | [dsys_mutangwan](https://github.com/ksamint/dsys_mutangwan) |
| 双囍烧腊 | [dsys_shuangxi-shaola](https://github.com/ksamint/dsys_shuangxi-shaola) |
| 港佬煲仔炉车仔面碟头饭 | [dsys_ganglao-baozailu](https://github.com/ksamint/dsys_ganglao-baozailu) |
| 小桃园 | [dsys_xiaotaoyuan](https://github.com/ksamint/dsys_xiaotaoyuan) |
| 苏帮袁 | [dsys_subangyuan](https://github.com/ksamint/dsys_subangyuan) |
| 游园京梦 | [dsys_youyuan-jingmeng](https://github.com/ksamint/dsys_youyuan-jingmeng) |
| 清水亭 | [dsys_qingshuiting](https://github.com/ksamint/dsys_qingshuiting) |

## Validation

Run `npm run build:site`, `npm run validate:routes`, and `python3 scripts/check-design-system-seed.py`. The seed check confirms that repository links reach both brand and IP records without replacing newer admin edits.
