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
```

## 共同背景基線

- 鎖雁關及朔北道的軍糧、關務、封存、查驗與商路後果可以延續，但不得把任一前作 branch 的人物命運、貨物物權或責任結論偷升格成全樹共同歷史。
- 《三更換囚》建立的換囚／軍糧案件只以實際存檔中的公開結果、責任認知與持續 state 帶入後作。
- 《鎖雁關外四車贖糧只夠三家》之後，合法發出的空官糧袋可以進入民間流轉；《斷柳坡…》的核心真相是有人利用舊包材洗白另一批貨，不是把前作補糧重新定義成失竊。
- 《鎖雁關北倉十二石封糧少了一張退封票》只在前作存檔實際保存相應封存貨物時才把十二石糧承接成同批貨；其他 ending 或無前作紀錄使用自身獨立封存批次，不令前作出關／失落／私下放行的貨物重新生成。
- 《鎖雁關南驗棚三甕留樣有一甕封泥沒壓繩結》只在北倉前案 state 實際支持同批貨進入後續複驗時承接批次 provenance；否則使用自身獨立留樣批次。本篇固定真相不因前作 ending 改寫。
- 《鎖雁關東交割棚四車糧袋只有一車沒沾秤盤灰》只在南驗棚存檔同時保存 `south-inspection-samples-cleared=true` 與該批貨依法完成複驗、進入後續交割的批次 receipt／provenance 時，才把四車視為同批後續交割；否則使用本篇獨立四車。無論入口如何，本篇固定真相均不因前作 ending 改寫。
- 《鎖雁關西稽棚七張放行票有一張墨色未乾》只在東交割棚存檔另有可驗證 receipt／provenance 顯示前案保全糧貨依法進入後續關務時，才可把本篇第五批涉案散糧視為同批後續清點中被重新分裝的部分；否則使用本篇獨立散糧批次。本篇合法補票與第五張篡改的固定真相不因前作 ending 改寫。

## Branch／state 路由

- 《關外四輛空車…》可讀取《三更換囚》既有 ending 作信任、程序與公開資訊 overlay；沒有前作紀錄時使用自身獨立基線。
- 《鎖雁關外四車…》可讀取《三更換囚》不同 ending，改變四車來源與公開責任背景，但不要求前作 NPC 必定存活或在場。
- 《斷柳坡…》可讀取 `four-carts-all-live`、`four-carts-law-first`、`four-carts-snowbound`、`four-carts-private-seizure` 等已保存結果；只帶入實際成立的發糧量、物權與公開責任。
- 《鎖雁關北倉十二石封糧少了一張退封票》直接讀取《斷柳坡…》ending：`nine-sacks-source-proved`／`nine-sacks-cart-held-source-unclear` 可令本篇十二石承接為同批封存貨；其餘不保證入北倉的 ending 使用本篇獨立批次，只帶入實際公開紀錄、辦案履歷與名譽。
- 《鎖雁關南驗棚三甕留樣有一甕封泥沒壓繩結》直接讀取北倉前案 state；只有實際支持同批貨進入後續複驗者才承接 provenance，其餘使用獨立批次並只改變程序態度／背景。
- 《鎖雁關東交割棚四車糧袋只有一車沒沾秤盤灰》直接讀取南驗棚 state；只有 `south-inspection-samples-cleared` 且另有同批貨依法進入交割的 receipt／provenance 時承接同批，其餘使用獨立批次並只改程序態度／成本。
- 《鎖雁關西稽棚七張放行票有一張墨色未乾》直接讀取東交割棚 state：`east-transfer-chain-cleared` 只有在另有可驗證批次 receipt／provenance 時才可承接同批散糧；`east-transfer-grain-held-unclear`、`east-transfer-records-lost`、`east-transfer-abandoned` 使用獨立批次並只改官面程序與信任；`east-transfer-wrong-cart-blamed` 只有在公開可知時令西稽棚更警惕「表面異常即等於有罪」的錯誤。前作 state 不改寫本篇固定真相。
- 同一來源 ending 若同時令多個後續成立，不因此自動互斥；後續能否先後遊玩只由實際 state 衝突決定。

## 本篇新增 state

《鎖雁關北倉十二石封糧少了一張退封票》依實際 ending 保存：
- `north-granary-chain-cleared`：本批保管鏈已重建，兩袋調換有官面紀錄。
- `north-granary-held-unclear`：貨物被保全，但責任鏈仍待補查。
- `north-granary-clerk-blamed`：書吏承擔錯置責任；不得把此結果升格成全樹共同正史。
- `north-granary-records-lost`：本批責任來源不足；若角色公開主動毀證，另保存 `north-granary-records-destroyed-by-pc=true`。
- `north-granary-private-settlement-secret`／`north-granary-private-settlement-exposed`：兩者互斥。
- `north-granary-abandoned`：本篇被明確放棄。

《鎖雁關南驗棚三甕留樣有一甕封泥沒壓繩結》依實際 ending 保存：
- `south-inspection-samples-cleared`：真留樣已保全，程序疏失與實際調換已能分辨。
- `south-inspection-held-unclear`：車／甕已保全，但責任鏈仍待續查。
- `south-inspection-kudian-blamed`：夜值庫工被錯扣責；不得升格成全樹共同正史。
- `south-inspection-records-lost`：關鍵證物未能形成可交接鏈；若角色主動毀證且可確認，另存 `south-inspection-records-destroyed-by-pc=true`。
- `south-inspection-private-settlement-secret`／`south-inspection-private-settlement-exposed`：兩者互斥。
- `south-inspection-abandoned`：本篇被明確放棄。

《鎖雁關東交割棚四車糧袋只有一車沒沾秤盤灰》依實際 ending 保存：
- `east-transfer-chain-cleared`：丁車合法側秤、乙車秤後減載及三袋去向已形成可交接證據鏈。
- `east-transfer-grain-held-unclear`：三袋／相關車輛已保全，但程序或責任仍有一部分待查。
- `east-transfer-wrong-cart-blamed`：丁車合法側秤被錯判為主要舞弊來源；不得升格成全樹共同正史。
- `east-transfer-records-lost`：本篇責任來源不足；若角色主動毀證且可確認，另保存 `east-transfer-records-destroyed-by-pc=true`。
- `east-transfer-abandoned`：本篇被明確放棄。

《鎖雁關西稽棚七張放行票有一張墨色未乾》依實際 ending 保存：
- `west-inspection-chain-cleared`：合法補票與第五張篡改已分清，兩只糧筐及責任鏈形成可交接記錄。
- `west-inspection-liability-found-cargo-lost`：篡改責任已有可靠來源，但兩只糧筐未在本篇內保全。
- `west-inspection-wrong-pass-blamed`：第七張合法補票被錯判為主要偽票；不得升格成全樹共同正史。
- `west-inspection-records-lost`：本篇票據責任鏈不足；若角色主動毀證且可確認，另保存 `west-inspection-records-destroyed-by-pc=true`。
- `west-inspection-private-settlement-secret`／`west-inspection-private-settlement-exposed`：若實際收賄私放，依是否已被共同消息網可靠歸因二擇一保存，兩者互斥。
- `west-inspection-abandoned`：本篇被明確放棄。

目前 `west-inspection-*` state **不對應任何尚未交付的具名後續**；只保留給本樹未來任務作可驗證來源。目錄不得因此暗示已有新劇本或自動關閉其他無互斥條件的節點。

## 維護

新增本樹任務時，更新本檔的節點、直接邊、共同背景與可達 state；不得移動或複製既有劇本檔來表達關連。