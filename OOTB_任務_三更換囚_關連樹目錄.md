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

## 關連圖

```text
三更換囚
├─→ 關外四輛空車都掛著滿載封牌
└─→ 鎖雁關外四車贖糧只夠三家
    └─→ 斷柳坡雪化後多了九只官糧袋
        └─→ 鎖雁關北倉十二石封糧少了一張退封票
```

## 共同背景基線

- 鎖雁關及朔北道的軍糧、關務、封存、查驗與商路後果可以延續，但不得把任一前作 branch 的人物命運、貨物物權或責任結論偷升格成全樹共同歷史。
- 《三更換囚》建立的換囚／軍糧案件只以實際存檔中的公開結果、責任認知與持續 state 帶入後作。
- 《鎖雁關外四車贖糧只夠三家》之後，合法發出的空官糧袋可以進入民間流轉；《斷柳坡…》的核心真相是有人利用舊包材洗白另一批貨，不是把前作補糧重新定義成失竊。
- 《鎖雁關北倉十二石封糧少了一張退封票》只在前作存檔實際保存相應封存貨物時才把十二石糧承接成同批貨；其他 ending 或無前作紀錄使用自身獨立封存批次，不令前作出關／失落／私下放行的貨物重新生成。

## Branch／state 路由

- 《關外四輛空車…》可讀取《三更換囚》既有 ending 作信任、程序與公開資訊 overlay；沒有前作紀錄時使用自身獨立基線。
- 《鎖雁關外四車…》可讀取《三更換囚》不同 ending，改變四車來源與公開責任背景，但不要求前作 NPC 必定存活或在場。
- 《斷柳坡…》可讀取 `four-carts-all-live`、`four-carts-law-first`、`four-carts-snowbound`、`four-carts-private-seizure` 等已保存結果；只帶入實際成立的發糧量、物權與公開責任。
- 《鎖雁關北倉十二石封糧少了一張退封票》直接讀取《斷柳坡…》ending：`nine-sacks-source-proved`／`nine-sacks-cart-held-source-unclear` 可令本篇十二石承接為同批封存貨；`nine-sacks-wrong-arrests`、`nine-sacks-cart-gone`、`nine-sacks-paid-passage`、`nine-sacks-abandoned` 等不保證該批貨入北倉，故使用本篇獨立批次，只帶入實際公開紀錄、辦案履歷與名譽。
- 同一來源 ending 若同時令多個後續成立，不因此自動互斥；後續能否先後遊玩只由實際 state 衝突決定。

## 本篇新增 state

《鎖雁關北倉十二石封糧少了一張退封票》依實際 ending 保存：
- `north-granary-chain-cleared`：本批保管鏈已重建，兩袋調換有官面紀錄。
- `north-granary-held-unclear`：貨物被保全，但責任鏈仍待補查。
- `north-granary-clerk-blamed`：書吏承擔錯置責任；不得把此結果升格成全樹共同正史。
- `north-granary-records-lost`：本批責任來源不足；若角色公開主動毀證，另保存 `north-granary-records-destroyed-by-pc=true`。
- `north-granary-private-settlement-secret`／`north-granary-private-settlement-exposed`：兩者互斥，分別表示私人放行未被共同消息網可靠歸因／已可靠公開歸因。
- `north-granary-abandoned`：本篇被明確放棄。

目前上述 state **不對應任何尚未交付的具名後續**；只保留給本樹未來任務作可驗證來源。目錄不得因此暗示已有新劇本或自動關閉其他無互斥條件的節點。

## 維護

新增本樹任務時，更新本檔的節點、直接邊、共同背景與可達 state；不得移動或複製既有劇本檔來表達關連。