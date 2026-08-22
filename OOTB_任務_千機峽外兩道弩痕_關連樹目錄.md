# 《千機峽外兩道弩痕》關連樹目錄

> 關係索引文檔；不是資料夾、不是固定戰役。

- **根任務**：《千機峽外兩道弩痕》
- **根 `script_id`**：`ootb-task-qianjixia-wai-liangdao-nuhen-v1`

## 節點

| 劇本 | `script_id` | 直接來源 | 關連定位 | 前作要求 |
|---|---|---|---|---|
| 《千機峽外兩道弩痕》 | `ootb-task-qianjixia-wai-liangdao-nuhen-v1` | — | 根任務 | 無 |
| 《回收帖上多了三個村名》 | `ootb-related-qianji-recall-three-villages-001` | 《千機峽外兩道弩痕》 | 後續／器械責任與回收制度承接 | 非必要；可獨立運行 |

## 關連圖

```text
千機峽外兩道弩痕
└─→ 回收帖上多了三個村名
```

## 共同背景與 state

- 天機閣「器有其主，技有其責」及事故後的器械責任／回收警覺可延續；不因關連新增門派高層或改寫正式制度。
- 後作可讀取 `qianji-end-01-tools-and-responsibility`、`qianji-end-02-danger-stopped-case-open`、`qianji-end-03-one-side-protected`、`qianji-end-04-evidence-lost`、`qianji-end-05-third-trigger-fires`、`qianji-end-06-abandon` 等保存結果作 overlay。
- 前作 NPC 可按存檔再出場，但不是後作唯一必要情報源；無前作存檔時使用新 NPC／本篇證據完成同一核心功能。

## 維護

後續若同時承接本樹其他新節點，應明列多來源與 state 相容性；不得只寫其中一個 anchor。