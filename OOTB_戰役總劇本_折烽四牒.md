# OOTB 戰役總劇本：折烽四牒

## 規格頭
- 戰役名：折烽四牒
- `campaign_id`：`ootb_campaign_broken_beacon_four_dispatches_v1`
- 總劇本版本：1.0.0
- 戰役狀態：連載中
- 規劃階段：4；目前正式階段：0／4。
- 共同起點：劍南道北緣山驛、關道與軍民共用的烽遞線。
- 等級／規模走向：第1篇4–7級中型 → 第2篇5–8級中型 → 第3篇6–9級大型 → 第4篇7–10級大型。
- 共用世界權威：Handbook 世界知識庫之時代與世界基準、昊國地理；只使用劍南道作區域基準，不固定未經權威文件確認的歷史名人。
- repository／桌次分工：本檔保存作者權威跨篇真相、actor、NPC registry、campaign state、接口與收束；單桌姓名、傷亡、證物持有與已宣告路線只存 `campaign_save`。

## 一、跨篇核心答案
山驛近月四次「急牒先到、烽火後起」不是敵軍滲透。北線轉運承辦 `<NPC#2@戰役:折烽四牒: 姓?-名?>` 利用軍民共用驛路的兩套登記時鐘，把本應在關口驗過的商貨夾進急牒車隊。驛丞 `<NPC#1@戰役:折烽四牒: 姓?-名?>` 最初只為替缺馬班次補簿，後來收錢提前蓋時刻。巡烽校尉 `<NPC#3@戰役:折烽四牒: 姓?-名?>` 察覺時刻矛盾後沒有上報，私下故意延後一座烽臺的點火，想看哪支車隊會趁「尚未警戒」的空窗通過。承辦人察覺有人放線，遂買通山口繩橋管事 `<NPC#4@戰役:折烽四牒: 姓?-名?>`，準備在末篇把最後一批帳牒與貨拆開送過封道線。

四「牒」依次是驛站急牒、車隊載貨牒、烽臺值更牒、山口封道牒。任何單份都只能證明局部失職。戰役要求玩家逐步分清補簿舞弊、貨運責任、越權放線與最後轉運，避免把所有異常錯歸於單一人物。

戰役開始前已成立：`<NPC#1>` 已提前蓋過三次時刻；`<NPC#2>` 已完成兩次夾貨並安排最後一批；`<NPC#3>` 已私改一次點烽順序；`<NPC#4>` 已收訂金但尚未動橋。玩家介入後的拘押、合作、證物存亡、封道與最後貨去向均為條件式未來。

玩家完全不介入：第一篇被判抄簿錯誤；第二篇夾貨完成；第三篇責任集中到越權校尉；第四篇最後帳牒越過山口，之後制度漏洞雖封閉，完整責任鏈難以證明。

## 二、主要行動者
### `actor_carrier` — `<NPC#2@戰役:折烽四牒: 姓?-名?>`
北線轉運承辦。知道兩套時鐘、夾貨車與最後批次；不知道校尉完整放線方法。利益是保住承辦權、現銀與可切割性。資源為車夫、貨棧、兩支合法急運車隊、現銀與路況。`carrier_alert=high` 時拆分帳牒；`last_load=detained` 時放棄貨保帳；被捕／死亡後已發出的車隊命令仍執行，直到正式封道或車夫自行退縮。

### `actor_postmaster` — `<NPC#1@戰役:折烽四牒: 姓?-名?>`
山驛驛丞。知道三次提前蓋時刻及付款來源；不知道最後橋務與校尉放線。利益是保住家計並避免成為主謀替罪羊。兩項獨立物證固定其有限責任後會合作；失去本人時由印簿、換馬牌與值房副簿承接。

### `actor_beacon` — `<NPC#3@戰役:折烽四牒: 姓?-名?>`
巡烽校尉。知道烽臺時刻矛盾與自己的越權延火；誤以為山口存在長期內應。利益是抓完整鏈並保住職位。`beacon_sting=stopped` 時交出值更牒；`exposed` 時退出主辦；死亡／失蹤由兩名烽卒與封存值更牒承接。

### `actor_bridge` — `<NPC#4@戰役:折烽四牒: 姓?-名?>`
山口繩橋管事。只知道有人付錢要求在指定時段把「封道」牌晚掛半刻，不知道前三篇全貌。利益是還債且不背軍務重罪。若看到正式封道文書或付款者已被捕，會猶豫並可被說服停止。

## 三、戰役級 NPC registry
| key | actor | 姓名約束 | 首次正式登場 | 跨篇功能 |
|---|---|---|---|---|
| `NPC#1@戰役:折烽四牒` | `actor_postmaster` | `姓?-名?` | 第1篇 | 補簿責任、時刻來源 |
| `NPC#2@戰役:折烽四牒` | `actor_carrier` | `姓?-名?` | 第1篇 | 主要轉運組織者 |
| `NPC#3@戰役:折烽四牒` | `actor_beacon` | `姓?-名?` | 第2篇 | 越權放線與烽牒來源 |
| `NPC#4@戰役:折烽四牒` | `actor_bridge` | `姓?-名?` | 第3篇 | 末段封道接口 |

## 四、campaign state registry
- `dispatch_chain = none / partial / strong`：跨篇牒證鏈強度；初始 `none`。
- `postmaster_status = free / cooperative / detained / gone`：初始 `free`。
- `carrier_alert = low / high`：初始 `low`。
- `beacon_sting = active / stopped / exposed`：初始 `active`。
- `bridge_status = normal / compromised / secured`：初始 `normal`。
- `last_load = planned / rerouted / detained / escaped`：初始 `planned`。
- `campaign_status = active / partly_completed / failed / completed`：初始 `active`。
- `campaign_progress`：初始 `0/4`；每篇正式結算後更新。

## 五、階段接口
### 第1篇《山驛四封急牒有一封比馬早到》— 連載中
- 預定 `script_id`：`ootb_campaign_broken_beacon_s1_early_dispatch_v1`；正式檔名：`OOTB_戰役任務_折烽四牒(1)_山驛四封急牒有一封比馬早到.md`。
- 帶入：全部初始 state；NPC#1、#2。
- 為甚麼現在：第四封急牒的蓋印時刻早於換馬牌實際到站，值房無法封簿。
- 為甚麼玩家：驛路監理需要不隸屬本班值房的外查者在下一輪車隊出發前核對。
- 任務：判定時刻矛盾成因、保全牒證、處理本班出發。
- 局部真相：NPC#1 提前蓋印，NPC#2 原擬用下一匹補到的驛馬與真車隊把帳面做平。
- 跨篇接觸：首次固定「同一車號在兩套時鐘中不一致」。
- 可改變：`dispatch_chain`、`postmaster_status`、`carrier_alert`、`campaign_progress`。
- endings：`s1_chain_open` → `dispatch_chain=partial`、`carrier_alert=high`、`campaign_status=active`、`campaign_progress=1/4`，承接第2篇；`s1_quiet_proof` → `partial`、`carrier_alert=low`、active、1/4，承接第2篇；`s1_false_close` → `none`、`campaign_status=partly_completed`、1/4，提早收束《驛簿已封》：眼前爭議完成，但玩家未取得可追的車隊接口；`s1_abandon` → failed、1/4，戰役終止。

### 第2篇《兩輛急運車都掛著同一塊載貨牌》— 規劃中
- 預定 `script_id`：`ootb_campaign_broken_beacon_s2_duplicate_load_v1`；正式檔名：`OOTB_戰役任務_折烽四牒(2)_兩輛急運車都掛著同一塊載貨牌.md`。
- 解鎖：第1篇 ending 為 `s1_chain_open OR s1_quiet_proof`；結算時一次判定並保存。
- 帶入：`dispatch_chain=partial`、`carrier_alert`、`postmaster_status`；NPC#2、#3。
- 為甚麼現在：同車號的兩輛急運車在不同關卡同時被記錄。
- 玩家理由：第1篇已取得車號／承辦接口，被要求沿車隊核對。
- 任務：分辨真急運與夾貨車，處理即將過關的兩車。
- 局部真相：NPC#2 以合法急運牌輪換掩護未驗商貨；NPC#3 正暗中放其中一車。
- 跨篇接觸：吃重與時刻把驛牒連到烽臺值更牒。
- 輸出：`dispatch_chain` 可 strong；`beacon_sting` 可 stopped/exposed；`carrier_alert` high。
- endings：`s2_two_clocks` → strong、active、2/4，承接第3篇；`s2_load_only` → partial、active、2/4，承接第3篇但開場證據較弱；`s2_wrong_master` → partly_completed、2/4，提早收束《扣住了車，斷了線》；`s2_abandon` → failed、2/4。

### 第3篇《三座烽臺有一座總慢半刻》— 規劃中
- 預定 `script_id`：`ootb_campaign_broken_beacon_s3_late_beacon_v1`；正式檔名：`OOTB_戰役任務_折烽四牒(3)_三座烽臺有一座總慢半刻.md`。
- 解鎖：第2篇 ending 為 `s2_two_clocks OR s2_load_only`；另讀第1篇保存的 `carrier_alert`，不重新判第1篇。
- 帶入：`dispatch_chain`、`carrier_alert`、`beacon_sting`、NPC#2、#3、#4。
- 為甚麼現在：玩家追到烽牒後發現第三臺的點火總比鄰臺慢半刻，且末批車隊正要利用同一空窗。
- 玩家理由：已有合法查車／牒證接口；烽臺值房要求在封道前釐清延火是失職還是內應。
- 任務：查清延火責任、決定是否停止放線、保住山口封道能力。
- 局部真相：NPC#3 越權延火追車；NPC#2 察覺後才另買通 NPC#4，兩者不是同夥。
- 輸出：`beacon_sting`、`bridge_status`、`last_load`、`dispatch_chain`。
- endings：`s3_split_fault` → `bridge_status=compromised`、`last_load=rerouted`、active、3/4，承接第4篇；`s3_secure_road` → `bridge_status=secured`、`last_load=detained`、active、3/4，承接第4篇以帳牒追收為入口；`s3_blame_beacon` → partly_completed、3/4，提早收束《烽火復明，山口無證》；`s3_abandon` → failed、3/4。

### 第4篇《山口兩道封牒只剩一道還算數》— 規劃中
- 預定 `script_id`：`ootb_campaign_broken_beacon_s4_last_pass_v1`；正式檔名：`OOTB_戰役任務_折烽四牒(4)_山口兩道封牒只剩一道還算數.md`。
- 解鎖：第3篇 `s3_split_fault OR s3_secure_road`；並載入既存 `dispatch_chain`、`carrier_alert`、`bridge_status`、`last_load`。
- 為甚麼現在：最後帳牒與貨已分路，封道命令只有一次有效窗口。
- 玩家理由：前三篇已建立合法調查與山口接口。
- 任務：處理最後貨、帳牒與責任鏈，正式收束戰役。
- 局部真相：NPC#4 只受買通晚掛封道牌；核心組織仍是 NPC#2，NPC#3 的越權另案處理。
- 末篇所有正式 ending 均 `campaign_progress=4/4`；完成完整責任鏈為 completed，證據不足但封住漏洞為 partly_completed，放棄／最後貨與帳證皆失且無法合理重建為 failed。

## 六、提早收束與失效回歸
- 任一人物死亡／失蹤不得抹除既有物證：NPC#1 → 印簿＋換馬牌；NPC#2 → 貨棧副帳＋車夫兩份獨立記錄；NPC#3 → 值更牒＋兩名烽卒；NPC#4 → 訂金包封＋橋務值牌。
- 關鍵物證若被毀，另一來源仍可證明局部結論；若同一必要結論的所有來源均合理永久失去，當篇必須進對應證據不足／失敗 ending，不憑空補新證據。
- `partly_completed` 收束一律先完成當篇眼前危機與人物結果，再以玩家可見但不揭核心答案的異常尾巴結束；其餘未觸發 future state 凍結，已成立 NPC 傷亡、證物持有與公開責任照實保存。

## 七、擴張邊界
後續版本不得把 NPC#3 改成走私同夥、不得把 NPC#4 改成前三篇既有內應，也不得推翻 NPC#1 的有限補簿責任。若新增第5篇，必須先更新本總綱、版本與正式接口，再重新通過總綱檢查。