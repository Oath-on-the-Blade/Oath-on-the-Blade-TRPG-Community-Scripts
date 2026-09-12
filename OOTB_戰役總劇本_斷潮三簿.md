# OOTB 戰役總劇本：斷潮三簿

## 規格頭
- 戰役名：斷潮三簿
- `campaign_id`：`ootb_campaign_broken_tide_three_ledgers_v1`
- 總劇本版本：1.1.0
- 戰役狀態：作者稿已完成，待整體覆檢／整合
- 已完成階段：4／4
- 規劃階段：
  1. 《潮倉三本簿有一本總比貨早到》— 6–9級、中型
  2. 《兩艘空船都報了滿艙吃水》— 7–10級、中型
  3. 《海陵三道驗牒有一道只認舊印》— 8–11級、大型
  4. 《定潮島外五盞引航燈有一盞不照船》— 9–12級、大型
- 共同起點：西海道海陵及蒼龍灣沿岸；末篇延伸至定潮島外主航道。
- 共用世界權威：Handbook `世界知識庫/地理與世界基準/時代與世界基準.md`、`世界知識庫/地理與世界基準/昊國地理.md`。海陵為西海道大城，設水師、海關、鹽運與造船場；蒼龍門山門在定潮島。
- repository 與桌次狀態分工：本檔保存作者權威的跨篇真相、NPC registry、state、接口與承接規則；實際桌次姓名、死亡／失蹤、已宣告承接與例外只寫入該桌 `campaign_save`。

## 一、跨篇核心答案（GM／作者）
海陵近月的錯簿、假吃水、舊驗印與錯引航，源自一條合法「退潮急轉倉」制度被不同人物各自利用。暴潮毀外碼頭後，海關容許已驗貨物先以臨時轉倉簿入內港，正簿稍後補齊。

海關轉倉書吏 `<NPC#1@戰役:斷潮三簿: 姓?-名?>` 先替熟船插隊收取小利，後被船盟外包貨棧掌櫃 `<NPC#2@戰役:斷潮三簿: 姓?-名?>` 利用，開始提前填臨簿時間。`<NPC#2>` 再用空船號、真貨船與數小時補數窗口，替未完稅海貨取得短暫合法外觀。

海關巡驗副手 `<NPC#3@戰役:斷潮三簿: 姓?-名?>` 從吃水與簿面差異察覺異常，卻誤判引航端存在穩定內應。他私留一枚已停用真驗印，讓可疑船過驗後暗跟，沒有上級授權。`<NPC#2>` 察覺放線後，買通普通夜間燈役 `<NPC#4@戰役:斷潮三簿: 姓?-名?>`，只要求在指定夜潮把一盞「候驗」燈改成「可入內灣」。蒼龍門及整個引航制度沒有參與走私。

三本「簿」分別是轉倉臨簿、船艙載貨簿、海關驗牒／印簿；任何一本都不足以單獨證明完整責任鏈。戰役核心是玩家能否在制度空窗被封閉、證據被切碎前，重建各人的有限責任，處理最後一批貨與帳證。

## 二、跨篇真實時間線
1. 承泰二十一年春末兩次暴潮毀外碼頭，海關啟用既有急轉倉流程。
2. `<NPC#1>` 由插隊舞弊逐步替 `<NPC#2>` 提前臨簿時間。
3. `<NPC#2>` 用空船號／真貨補數完成三次遮掩，開始處理高價未完稅海貨。
4. `<NPC#3>` 發現吃水與簿面矛盾，私留舊驗印放線。
5. `<NPC#2>` 察覺有人放線，拆分帳證並準備最後船。
6. `<NPC#2>` 支付 `<NPC#4>` 3兩訂金，要求末篇夜潮改第三盞燈。
7. 玩家完全不介入時：第一篇被當抄錄失誤；第二篇貨物轉移；第三篇責任集中到越權副手；第四篇錯燈讓最後帳證離港，制度漏洞之後雖被封，完整責任鏈難以證明。

## 三、主要行動者
### `actor_shipbroker` — `<NPC#2@戰役:斷潮三簿: 姓?-名?>`
- 身份：船盟外包貨棧掌櫃；主要組織者。
- 知道：急轉倉空窗、可收買船戶、`<NPC#1>` 可改時間。
- 不知道：`<NPC#3>` 放線完整計畫。
- 利益：保住貨棧、人脈與現銀。
- 資源：貨棧、腳夫、兩名可信船戶、現銀、潮時知識。
- 限制：不能控制海關或蒼龍門；每次假簿仍需真貨補數。
- 反應：警覺升高便拆證、換船；被捕／死亡後，已發出的付款與船戶安排仍會運行。

### `actor_clerk` — `<NPC#1@戰役:斷潮三簿: 姓?-名?>`
- 身份：海關轉倉書吏。
- 知道：自己改過的時刻、收款與指定船號。
- 不知道：舊印放線、錯燈、最終收貨全貌。
- 利益：保住家計並避免替 `<NPC#2>` 扛下全部責任。
- 限制：不能改碼頭實際進出、倉戶時刻與船體吃水。

### `actor_deputy` — `<NPC#3@戰役:斷潮三簿: 姓?-名?>`
- 身份：海關巡驗副手。
- 知道：吃水矛盾、自己越權私留舊印。
- 誤解：引航端有穩定內應網。
- 利益：抓完整責任鏈與保職衝突。
- 限制：無正式密令；舊印曝光即損害職位與證據可信度。

### `actor_pilots`／`<NPC#4@戰役:斷潮三簿: 姓?-名?>`
- 引航制度公開利益是航道安全與燈號可信。
- `<NPC#4>` 只是欠債後接受一次性3兩訂金的普通夜間燈役；不知道三簿全貌，不代表蒼龍門。

## 四、戰役級 NPC registry
| key | 姓名欄 | 跨篇功能 | actor_key | 首次正式登場 |
|---|---|---|---|---|
| `NPC#1@戰役:斷潮三簿` | `姓?-名?` | 海關轉倉書吏；第一本簿入口 | `actor_clerk` | 第1篇 |
| `NPC#2@戰役:斷潮三簿` | `姓?-名?` | 船盟外包貨棧掌櫃；主要組織者 | `actor_shipbroker` | 第1篇 |
| `NPC#3@戰役:斷潮三簿` | `姓?-名?` | 海關巡驗副手；越權放線者 | `actor_deputy` | 第1篇 |
| `NPC#4@戰役:斷潮三簿` | `姓?-名?` | 普通夜間燈役；錯燈執行者 | 無 | 第3篇建立接口、第4篇正式處理 |

編號永久保留；不得由後篇另配本地 NPC 編號取代。

## 五、campaign state registry
| state | 值 | 初始值 | 來源／用途 |
|---|---|---|---|
| `ledger_chain` | `none / partial / strong` | `none` | 第1–4篇；三簿互證強度 |
| `clerk_status` | `free / cooperating / detained / fled / dead` | `free` | 第1篇起；書吏能否作證 |
| `broker_alert` | `low / high` | `low` | 第1–3篇；拆證／換船 |
| `deputy_sting` | `active / stopped / exposed` | `active` | 第1–3篇；舊印放線狀態 |
| `old_seal_secured` | bool | `false` | 第3篇；舊印是否依法保存 |
| `lamp_link` | `unknown / suspected / identified` | `unknown` | 第3–4篇；燈役接口強度 |
| `final_ship` | `scheduled / rerouted / detained / sailed` | `scheduled` | 第2–4篇；末篇船與帳證位置 |
| `pilot_trust` | `neutral / cooperative / hostile` | `neutral` | 第3–4篇；引航端合作程度 |
| `campaign_status` | `active / partly_completed / failed / completed` | `active` | 每篇正式結算 |

## 六、階段接口與 ending 映射
### 第1篇《潮倉三本簿有一本總比貨早到》— 已完成
- 獨立目標：查清本次「簿早於貨」的直接原因並處理缺貨責任。
- `bt1_documented`：`ledger_chain=partial`；可承接第2篇，`campaign_status=active`。
- `bt1_clerk_only`：只證明 `<NPC#1>` 個人偽簿；可承接第2篇，`campaign_status=active`。
- `bt1_false_clean`：沒有可追接口；提早部分完成，`campaign_status=partly_completed`，`campaign_progress=1/4`。
- `bt1_abandon`：提早失敗，`campaign_status=failed`，`campaign_progress=1/4`。

### 第2篇《兩艘空船都報了滿艙吃水》— 已完成
- 解鎖：`(bt1_documented OR bt1_clerk_only) AND campaign_status=active`；開局只載入已宣告承接。
- `bt2_chain`：`ledger_chain=strong`；可承接第3篇。
- `bt2_stop_cargo`：`ledger_chain=partial`、`broker_alert=high`、`final_ship=rerouted`；可承接第3篇。
- `bt2_wrong_ship`：沒有可追舊印／貨棧接口；提早部分完成，`campaign_status=partly_completed`，`campaign_progress=2/4`。
- `bt2_abandon`：提早失敗，`campaign_status=failed`，`campaign_progress=2/4`。

### 第3篇《海陵三道驗牒有一道只認舊印》— 已完成
- 解鎖：`(bt2_chain OR bt2_stop_cargo) AND campaign_status=active`，並保留更早仍有效 state。
- `bt3_sting_stopped`：`old_seal_secured=true`、`deputy_sting=stopped`；可承接第4篇。
- `bt3_sting_exposed`：`deputy_sting=exposed`、`broker_alert=high`、通常 `final_ship=rerouted`；可承接第4篇。
- `bt3_blame_pilots`：引航端資料接口失去；提早部分完成，`campaign_status=partly_completed`，`campaign_progress=3/4`。
- `bt3_abandon`：提早失敗，`campaign_status=failed`，`campaign_progress=3/4`。

### 第4篇《定潮島外五盞引航燈有一盞不照船》— 已完成（末篇）
- 解鎖：`(bt3_sting_stopped OR bt3_sting_exposed) AND campaign_status=active`；帶入 `ledger_chain`、`broker_alert`、`old_seal_secured`、`lamp_link`、`final_ship`、`pilot_trust` 及戰役 NPC 狀態。
- `bt4_chain_closed`：錯燈與最後船／代用品受控，責任鏈完整；`campaign_status=completed`，`campaign_progress=4/4`。
- `bt4_harbor_saved`：當夜危機解決但責任鏈只有 partial；原定路線已到末篇，`campaign_status=completed`，`campaign_progress=4/4`。
- `bt4_false_signal`：錯燈一度成功但之後救回人船或固定部分責任；原定路線正式收束，`campaign_status=completed`，`campaign_progress=4/4`。
- `bt4_abandon`：放棄；`campaign_status=failed`，`campaign_progress=4/4`。

## 七、條件式反應
- `broker_alert=high`：`<NPC#2>` 提前拆帳證、改最後船號；潮時與付款痕跡不消失。
- `clerk_status=cooperating`：`<NPC#1>` 可提供自己實際改過的時刻與船號；仍需物證互證。
- `clerk_status=detained`：海關封存簿冊，以封存副本替代本人出場。
- `deputy_sting=active`：`<NPC#3>` 繼續舊印放線，直到第三篇處理。
- `deputy_sting=exposed`：其失去現場權限，既有證詞／差役記錄仍可用。
- `pilot_trust=hostile`：引航端要求正式公文；不刪除必要資料，只增加合法取得時間。
- `lamp_link=identified`：`<NPC#4>` 可能請假／換班；付款、輪值與遮片痕跡仍存在。

## 八、跨篇證物與回歸代用品
- 轉倉臨簿毀損：倉戶簽收時刻＋值房抄副互證；兩者同失才降級 `ledger_chain`。
- 載貨簿毀損：碼頭量水尺＋兩名不同班次裝卸人的貨量記憶互證；單一口供不能升 strong。
- 舊驗印丟失：印匣領用簿＋兩名差役證詞仍可證越權，無法作精細印痕比對。
- 燈役付款：貨棧支出副頁＋輪值交換互證；錢袋不是唯一證據。
- `<NPC#1>` 死亡／逃走：改筆與倉戶時刻保留其局部責任；後篇不得假裝其親口作證。
- `<NPC#3>` 死亡／失蹤：舊印與差役記錄處理放線責任。
- `<NPC#2>` 提前被捕／死亡：船戶、貨棧既定付款與最後船計畫照已成立 state 推進；本人不會越獄／復活。
- `<NPC#4>` 提前被拘押／死亡：錯燈不再由其親自執行；遮片、付款、輪值與跑腿描述仍可固定個人受賄；其口供不可再取得。
- 最後船已 `detained`：末篇轉為保護航道與固定責任鏈。
- 最後船已 `sailed`：不保證追上；以岸上證據處理較弱責任鏈，世界另行追船。

## 九、不得 retcon
1. 第1篇確定 `<NPC#1>` 偽造本次臨簿；後篇不得改成完全無責。
2. 第2篇確定空船號／真貨船交換；後篇只補誰利用及為何。
3. 第3篇舊印確由 `<NPC#3>` 越權私留；後篇不得改成 `<NPC#2>` 偽造同印。
4. 第4篇只有單一燈役受賄，不得升格成蒼龍門或整個引航制度參與走私。
5. 玩家造成的死亡、扣船、公開揭露與其他例外由 `campaign_save` 保存；後篇依 state 改場景，不回寫本檔假裝原本如此。

## 十、戰役完成與保存
原定四篇全部完成。前三篇不可承接 ending 已各自在當篇形成提早戰役結局；放棄一律終止。末篇正式結算保存 `ending_id`、`campaign_status`、`campaign_progress=4/4`、所有仍有效 state、四名戰役 NPC 最終狀態及最後副頁狀態。世界仍可有追責、追船與制度後果，但不自動新增第五篇。

作者完成末篇後，必須以本最終總綱＋四篇最終 md 執行 `戰役整體覆檢.md`；只有總綱、全部單篇 Phase B 與跨篇整體覆檢均通過，才可整合至 `main`。
