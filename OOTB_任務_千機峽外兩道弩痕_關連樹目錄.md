# 《千機峽外兩道弩痕》關連樹目錄

> 關係索引文檔；不是資料夾、不是固定戰役。

- **根任務**：《千機峽外兩道弩痕》
- **根 `script_id`**：`ootb-task-qianjixia-wai-liangdao-nuhen-v1`

## 節點

| 劇本 | `script_id` | 直接來源 | 關連定位 | 前作要求 |
|---|---|---|---|---|
| 《千機峽外兩道弩痕》 | `ootb-task-qianjixia-wai-liangdao-nuhen-v1` | — | 根任務 | 無 |
| 《回收帖上多了三個村名》 | `ootb-related-qianji-recall-three-villages-001` | 《千機峽外兩道弩痕》 | 後續／器械責任與回收制度承接 | 非必要；可獨立運行 |
| 《石梁驛三架貨鉤只有兩架敢起吊》 | `ootb-related-shiliang-three-hoists-001` | 《千機峽外兩道弩痕》 | 後續／器械責任與民間使用後果 | 非必要；可獨立運行 |

## 關連圖

```text
千機峽外兩道弩痕
├─→ 回收帖上多了三個村名
└─→ 石梁驛三架貨鉤只有兩架敢起吊
```

## 共同背景與 state

- 天機閣「器有其主，技有其責」及事故後的器械責任／回收警覺可延續；不因關連新增門派高層或改寫正式制度。
- 兩個目前後續節點是**可並存的兄弟節點**，不是互斥分支；完成其中一篇不會自動取消另一篇的合法入口。
- 《回收帖上多了三個村名》承接的是危險報廢器械回收制度被冒名利用的後果；《石梁驛三架貨鉤只有兩架敢起吊》承接的是民間把舊製作者印記、後續改裝與整機責任混為一談的後果。兩篇互不讀取彼此專用 `ending_id`／NPC／物件 state。
- 後作可讀取根任務 `qianji-end-01-tools-and-responsibility`、`qianji-end-02-danger-stopped-case-open`、`qianji-end-03-one-side-protected`、`qianji-end-04-evidence-lost`、`qianji-end-05-third-trigger-fires`、`qianji-end-06-abandon` 等保存結果作 overlay；每篇正文仍須自行列出實際使用的可執行映射。
- 前作 NPC 可按存檔再出場，但不是後作唯一必要情報源；無前作存檔時使用新 NPC／本篇證據完成同一核心功能。
- 《石梁驛三架貨鉤只有兩架敢起吊》若成立 `shiliang_hoist_load_test_recorded = true`，只保存石梁驛本地的「棘輪殼來源／後續換件／最近測重」分欄記錄，不自動升格為天機閣或雲東道全境制度；`shiliang_hoist_case_open = true` 亦只表示甲吊責任仍待後查。

## 維護

後續若同時承接本樹兩個以上節點，必須在新劇本正文明列多來源條件與 state 相容性；不得只寫其中一個 anchor，也不得把兄弟節點排版誤讀成互斥。