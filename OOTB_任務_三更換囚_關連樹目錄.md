# 《三更換囚》關連樹目錄

> 本檔是關連樹的**關係索引文檔**，不是劇本、不是資料夾，也不代表玩家必須按固定順序遊玩。各劇本正文仍是其客觀真相、`ending_id` 與運行資料的權威來源。

- **根任務**：《三更換囚》
- **根 `script_id`**：`ootb-sanjing-huanqiu`
- **樹內原則**：只建立本樹內關連；沒有跨樹直接關連。

## 節點與直接關連

| 劇本 | `script_id` | 直接來源 | 關連定位 | 前作要求 |
|---|---|---|---|---|
| 《三更換囚》 | `ootb-sanjing-huanqiu` | — | 根任務 | 無 |
| 《關外四輛空車都掛著滿載封牌》 | `ootb-guanwai-siliang-kongche` | 《三更換囚》 | 後續／後傳關連 | 非必要；可獨立運行 |
| 《鎖雁關外四車贖糧只夠三家》 | `ootb-linked-four-carts-redemption-grain-001` | 《三更換囚》 | 後續／分支承接 | 非必要；可獨立運行 |
| 《斷柳坡雪化後多了九只官糧袋》 | `ootb-linked-duanliu-nine-grain-sacks-001` | 《鎖雁關外四車贖糧只夠三家》 | 後續／貨物流向延伸 | 非必要；可獨立運行 |
| 《鎖雁關北倉十二石封糧少了一張退封票》 | `ootb-linked-suobei-north-granary-unseal-slip-001` | 《斷柳坡雪化後多了九只官糧袋》 | 後續／保管鏈延伸 | 非必要；可獨立運行 |
| 《鎖雁關南驗棚三甕留樣有一甕封泥沒壓繩結》 | `ootb-linked-suobei-south-inspection-three-sample-jars-001` | 《鎖雁關北倉十二石封糧少了一張退封票》 | 後續／複驗與留樣保管鏈延伸 | 非必要；可獨立運行 |
| 《鎖雁關東交割棚四車糧袋只有一車沒沾秤盤灰》 | `ootb-linked-suobei-east-transfer-four-carts-scale-dust-001` | 《鎖雁關南驗棚三甕留樣有一甕封泥沒壓繩結》 | 後續／複驗後交割與放行鏈延伸 | 非必要；可獨立運行 |
| 《鎖雁關西稽棚七張放行票有一張墨色未乾》 | `ootb-linked-suobei-west-inspection-seven-passes-wet-ink-001` | 《鎖雁關東交割棚四車糧袋只有一車沒沾秤盤灰》 | 後續／交割後放行與票據責任鏈延伸 | 非必要；可獨立運行 |
| 《鎖雁關外換輪棚六根車軸有一根沒有油泥》 | `ootb-linked-suobei-wheel-shed-six-axles-clean-001` | 《鎖雁關西稽棚七張放行票有一張墨色未乾》 | 後續／放行後貨物流向與車馬證據鏈延伸 | 非必要；可獨立運行 |

## 關連圖

```text
三更換囚
├─→ 關外四輛空車都掛著滿載封牌
└─→ 鎖雁關外四車贖糧只夠三家
    └─→ 斷柳坡雪化後多了九只官糧袋
        └─→ 鎖雁關北倉十二石封糧少了一張退封票
            └─→ 鎖雁關南驗棚三甕留樣有一甕封泥沒壓繩結
                └─→ 鎖雁關東交割棚四車糧袋只有一車沒沾秤盤灰
                    └─→ 鎖雁關西稽棚七張放行票有一張墨色未乾
                        └─→ 鎖雁關外換輪棚六根車軸有一根沒有油泥
```

## 共同背景基線

- 鎖雁關及朔北道的軍糧、關務、封存、查驗與商路後果可以延續，但不得把任一前作 branch 的人物命運、貨物物權或責任結論偷升格成全樹共同歷史。
- 《三更換囚》建立的換囚／軍糧案件只以實際存檔中的公開結果、責任認知與持續 state 帶入後作。
- 《鎖雁關外四車贖糧只夠三家》之後，合法發出的空官糧袋可以進入民間流轉；《斷柳坡…》的核心真相是有人利用舊包材洗白另一批貨，不是把前作補糧重新定義成失竊。
- 《鎖雁關北倉十二石封糧少了一張退封票》只在前作存檔實際保存相應封存貨物時才把十二石糧承接成同批貨；其他 ending 或無前作紀錄使用自身獨立封存批次，不令前作出關／失落／私下放行的貨物重新生成。
- 《鎖雁關南驗棚三甕留樣有一甕封泥沒壓繩結》只在北倉前案 state 實際支持同批貨進入後續複驗時承接批次 provenance；否則使用自身獨立留樣批次。本篇固定真相不因前作 ending 改寫。
- 《鎖雁關東交割棚四車糧袋只有一車沒沾秤盤灰》只在南驗棚存檔同時保存 `south-inspection-samples-cleared=true` 與該批貨依法完成複驗、進入後續交割的批次 receipt／provenance 時，才把四車視為同批後續交割；否則使用本篇獨立四車。無論入口如何，本篇固定真相均不因前作 ending 改寫。
- 《鎖雁關西稽棚七張放行票有一張墨色未乾》只在東交割棚存檔另有可驗證 receipt／provenance 顯示前案保全糧貨依法進入後續關務時，才可把本篇第五批涉案散糧視為同批後續清點中被重新分裝的部分；否則使用本篇獨立散糧批次。本篇合法補票與第五張篡改的固定真相不因前作 ending 改寫。
- 《鎖雁關外換輪棚六根車軸有一根沒有油泥》只有在西稽棚存檔保存 `west-inspection-liability-found-cargo-lost` 且另有可驗證第五批車號／車身記號時，才把第四車與兩只糧筐承接為前作同批貨；若 `west-inspection-chain-cleared` 已證明前作兩筐依法保全，本篇使用同一轉運手法涉及的另一批兩筐，絕不把已保全貨物重新生成。其他 state 或無前作紀錄使用本篇獨立批次。本篇「新軸合法、第四車轉貨」固定真相不因前作 ending 改寫。

## Branch／state 路由

- 《關外四輛空車…》可讀取《三更換囚》既有 ending 作信任、程序與公開資訊 overlay；沒有前作紀錄時使用自身獨立基線。
- 《鎖雁關外四車…》可讀取《三更換囚》不同 ending，改變四車來源與公開責任背景，但不要求前作 NPC 必定存活或在場。
- 《斷柳坡…》可讀取 `four-carts-all-live`、`four-carts-law-first`、`four-carts-snowbound`、`four-carts-private-seizure` 等已保存結果；只帶入實際成立的發糧量、物權與公開責任。
- 《鎖雁關北倉十二石封糧少了一張退封票》直接讀取《斷柳坡…》ending：`nine-sacks-source-proved`／`nine-sacks-cart-held-source-unclear` 可令本篇十二石承接為同批封存貨；其他 ending 不保證該批貨入北倉，故使用本篇獨立批次，只帶入實際公開紀錄、辦案履歷與名譽。
- 《鎖雁關南驗棚三甕留樣有一甕封泥沒壓繩結》直接讀取北倉 state：`north-granary-chain-cleared` 可在存檔另有批次依法進入後續複驗時承接同批 provenance；其他 state 預設使用本篇獨立批次，只按公開程度改變態度／背景，秘密私了不得自動揭露。
- 《鎖雁關東交割棚四車糧袋只有一車沒沾秤盤灰》直接讀取南驗棚 state：`south-inspection-samples-cleared` 只有在另有同批貨已依法進入交割的 receipt／provenance 時承接同批；其他 state 預設使用獨立批次並只改程序態度／成本。本篇真相不由前作 state 改寫。
- 《鎖雁關西稽棚七張放行票有一張墨色未乾》直接讀取東交割棚 state：`east-transfer-chain-cleared` 只有在另有可驗證批次 receipt／provenance 時才可承接同批散糧；其他 state 預設使用本篇獨立批次並只改官面程序與信任。`east-transfer-wrong-cart-blamed` 只在公開可知時令西稽棚更警惕「表面異常即等於有罪」。
- 《鎖雁關外換輪棚六根車軸有一根沒有油泥》直接讀取西稽棚 state：`west-inspection-liability-found-cargo-lost` + 可驗證第五批車號／車身記號時可承接同批兩筐；`west-inspection-chain-cleared` 使用另一批兩筐，只承接辦案履歷與轉運手法背景；`west-inspection-wrong-pass-blamed`、`west-inspection-records-lost`、`west-inspection-abandoned` 或無前作紀錄使用獨立批次。`west-inspection-private-settlement-secret` 必須保持秘密，只有 `...exposed` 可改變官面初始態度。
- 同一來源 ending 若同時令多個後續成立，不因此自動互斥；後續能否先後遊玩只由實際 state 衝突決定。

## 本篇新增 state

《鎖雁關北倉十二石封糧少了一張退封票》依實際 ending 保存：
- `north-granary-chain-cleared`
- `north-granary-held-unclear`
- `north-granary-clerk-blamed`
- `north-granary-records-lost`；角色主動毀證且可確認時另存 `north-granary-records-destroyed-by-pc=true`
- `north-granary-private-settlement-secret`／`north-granary-private-settlement-exposed`（互斥）
- `north-granary-abandoned`

《鎖雁關南驗棚三甕留樣有一甕封泥沒壓繩結》依實際 ending 保存：
- `south-inspection-samples-cleared`
- `south-inspection-held-unclear`
- `south-inspection-kudian-blamed`
- `south-inspection-records-lost`；角色主動毀證且可確認時另存 `south-inspection-records-destroyed-by-pc=true`
- `south-inspection-private-settlement-secret`／`south-inspection-private-settlement-exposed`（互斥）
- `south-inspection-abandoned`

《鎖雁關東交割棚四車糧袋只有一車沒沾秤盤灰》依實際 ending 保存：
- `east-transfer-chain-cleared`
- `east-transfer-grain-held-unclear`
- `east-transfer-wrong-cart-blamed`
- `east-transfer-records-lost`；角色主動毀證且可確認時另存 `east-transfer-records-destroyed-by-pc=true`
- `east-transfer-abandoned`

《鎖雁關西稽棚七張放行票有一張墨色未乾》依實際 ending 保存：
- `west-inspection-chain-cleared`
- `west-inspection-liability-found-cargo-lost`
- `west-inspection-wrong-pass-blamed`
- `west-inspection-records-lost`；角色主動毀證且可確認時另存 `west-inspection-records-destroyed-by-pc=true`
- `west-inspection-private-settlement-secret`／`west-inspection-private-settlement-exposed`（互斥）
- `west-inspection-abandoned`

《鎖雁關外換輪棚六根車軸有一根沒有油泥》依實際 ending 保存：
- `wheel-shed-chain-cleared`
- `wheel-shed-liability-found-cargo-lost`
- `wheel-shed-wrong-axle-blamed`
- `wheel-shed-trail-lost`；角色主動毀證且可確認時另存 `wheel-shed-records-destroyed-by-pc=true`
- `wheel-shed-abandoned`

目前 `wheel-shed-*` state 不對應任何尚未交付的具名後續；只保留給本樹未來任務作可驗證來源。

## 維護

新增本樹任務時，更新本檔的節點、直接邊、共同背景與可達 state；不得移動或複製既有劇本檔來表達關連。