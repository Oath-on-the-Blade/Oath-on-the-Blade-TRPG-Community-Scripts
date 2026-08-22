# 《三盞閘燈不能同時熄》關連樹目錄

> 關係索引文檔；不是資料夾、不是固定戰役。

- **根任務**：《三盞閘燈不能同時熄》
- **根 `script_id`**：`ootb-hard-sluice-three-lamps-001`

## 節點

| 劇本 | `script_id` | 直接來源 | 關連定位 | 前作要求 |
|---|---|---|---|---|
| 《三盞閘燈不能同時熄》 | `ootb-hard-sluice-three-lamps-001` | — | 根任務 | 無 |
| 《新閘六道泄洪槽只有五道見過水》 | `ootb-xinzha-liudao-xiehongcao` | 《三盞閘燈不能同時熄》 | 後續／水閘制度與責任承接 | 非必要；可獨立運行 |

## 關連圖

```text
三盞閘燈不能同時熄
└─→ 新閘六道泄洪槽只有五道見過水
```

## 共同背景與 state

- 前作的閘務事故可造成地方對放水程序、走私與證物保存的不同警覺，但後作本身的客觀事故原因不得由前作 ending 決定。
- 後作可讀取 `sluice-held-all`、`sluice-held-ship-gone`、`sluice-evidence-over-market`、`sluice-people-over-proof`、`sluice-collusion`、`sluice-abandon` 或無前作紀錄；這些只改變開場取得資料、信任與程序成本。
- 沒有前作存檔時使用後作自己的完整獨立基線。

## 維護

新增本樹分支時可由同一 ending 開啟多篇後續；除非正文建立明確互斥 state，否則不得因「同源分支」自動視為二選一。