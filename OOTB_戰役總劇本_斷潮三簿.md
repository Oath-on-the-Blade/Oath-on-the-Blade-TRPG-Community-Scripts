# OOTB 戰役總劇本：斷潮三簿

## 規格頭
- 戰役名：斷潮三簿
- `campaign_id`：`ootb_campaign_broken_tide_three_ledgers_v1`
- 總劇本版本：1.2.1
- 戰役狀態：已完結
- 原定階段：4／4；本版本無規劃中的第5階段。
- 戰役共同起點：西海道海陵及蒼龍灣沿岸；末篇延伸至定潮島外主航道。
- 預期等級／規模走向：第1篇6–9級中型 → 第2篇7–10級中型 → 第3篇8–11級大型 → 第4篇9–12級大型。
- 共用世界權威：Handbook `世界知識庫/地理與世界基準/時代與世界基準.md`、`世界知識庫/地理與世界基準/昊國地理.md`。海陵為西海道大城，設水師、海關、鹽運與造船場；蒼龍門山門在定潮島。
- repository 與桌次狀態分工：本檔只保存作者權威的跨篇真相、actor、戰役級 NPC registry、campaign state、階段接口、承接與收束規則；單桌實例姓名、死亡／失蹤、玩家實際持有物、已宣告承接路線及其他例外只寫入該桌 `campaign_save`，不得回寫成 repository 的固定歷史。

### 正式階段清單
| 序號 | 篇名 | `script_id` | 正式檔名 | 狀態 |
|---|---|---|---|---|
| 1 | 《潮倉三本簿有一本總比貨早到》 | `ootb_campaign_broken_tide_s1_early_ledger_v1` | `OOTB_戰役任務_斷潮三簿(1)_潮倉三本簿有一本總比貨早到.md` | 已完成；隨本戰役整合發布 |
| 2 | 《兩艘空船都報了滿艙吃水》 | `ootb_campaign_broken_tide_s2_false_draft_v1` | `OOTB_戰役任務_斷潮三簿(2)_兩艘空船都報了滿艙吃水.md` | 已完成；隨本戰役整合發布 |
| 3 | 《海陵三道驗牒有一道只認舊印》 | `ootb_campaign_broken_tide_s3_old_seal_v1` | `OOTB_戰役任務_斷潮三簿(3)_海陵三道驗牒有一道只認舊印.md` | 已完成；隨本戰役整合發布 |
| 4 | 《定潮島外五盞引航燈有一盞不照船》 | `ootb_campaign_broken_tide_s4_false_lamp_v1` | `OOTB_戰役任務_斷潮三簿(4)_定潮島外五盞引航燈有一盞不照船.md` | 已完成；末篇；隨本戰役整合發布 |

## 一、跨篇核心答案（GM／作者）
海陵近月的錯簿、假吃水、舊驗印與錯引航，源自一條合法「退潮急轉倉」制度被不同人物各自利用。暴潮毀外碼頭後，海關容許已驗貨物先以臨時轉倉簿入內港，正簿稍後補齊。

海關轉倉書吏 `<NPC#1@戰役:斷潮三簿: 姓?-名?>` 先替熟船插隊收取小利，後被船盟外包貨棧掌櫃 `<NPC#2@戰役:斷潮三簿: 姓?-名?>` 利用，開始提前填臨簿時間。`<NPC#2>` 再用空船號、真貨船與數小時補數窗口，替未完稅海貨取得短暫合法外觀。

海關巡驗副手 `<NPC#3@戰役:斷潮三簿: 姓?-名?>` 從吃水與簿面差異察覺異常，卻誤判引航端存在穩定內應。他私留一枚已停用真驗印，讓可疑船過驗後暗跟，沒有上級授權。`<NPC#2>` 察覺放線後，買通普通夜間燈役 `<NPC#4@戰役:斷潮三簿: 姓?-名?>`，只要求在指定夜潮把一盞「候驗」燈改成「可入內灣」。蒼龍門及整個引航制度沒有參與走私。

三本「簿」分別是轉倉臨簿、船艙載貨簿、海關驗牒／印簿；任何一本都不足以單獨證明完整責任鏈。戰役核心是玩家能否在制度空窗被封閉、證據被切碎前，重建各人的有限責任，並處理最後一批貨與帳證。

戰役開始前已成立的秘密只有：`<NPC#1>` 的提前臨簿、`<NPC#2>` 的船號補數、`<NPC#3>` 的越權舊印放線，以及 `<NPC#2>` 已對 `<NPC#4>` 發出一次性錯燈付款。玩家介入後誰被捕、誰合作、哪份證據仍在、最後船是否改泊或被扣，全部是條件式未來，不得寫死。

## 二、跨篇真實時間線
1. 承泰二十一年春末兩次暴潮毀外碼頭，海關啟用既有急轉倉流程。
2. `<NPC#1>` 由插隊舞弊逐步替 `<NPC#2>` 提前臨簿時間。
3. `<NPC#2>` 用空船號／真貨補數完成三次遮掩，開始處理高價未完稅海貨。
4. `<NPC#3>` 發現吃水與簿面矛盾，私留舊驗印放線。
5. `<NPC#2>` 察覺有人放線，拆分帳證並準備最後船。
6. `<NPC#2>` 支付 `<NPC#4>` 3兩訂金，要求末篇夜潮改第三盞燈。
7. 玩家完全不介入時：第一篇被當抄錄失誤；第二篇貨物轉移；第三篇責任集中到越權副手；第四篇錯燈讓最後帳證離港。制度漏洞之後雖被封，完整責任鏈難以證明。
8. 任何階段正式結算後，只依該桌 `campaign_save` 的 ending、state、人物／證物例外推進；不得用本時間線覆蓋玩家已造成的結果。

## 三、跨篇主要行動者

### `actor_shipbroker` — `<NPC#2@戰役:斷潮三簿: 姓?-名?>`
- 身份／位置：船盟外包貨棧掌櫃；主要組織者，活動於海陵外包貨棧與港區。
- 初始知道：急轉倉空窗、可收買船戶、`<NPC#1>` 可提前臨簿、最後船與付款安排。
- 初始不知道／誤解：不知道 `<NPC#3>` 放線的完整做法；起初低估玩家能把三本簿互證。
- 核心利益：保住貨棧、人脈、現銀及自己與走私鏈的可切割性。
- 當前計畫：用真貨補數把前兩本簿做平；一旦舊印或船號鏈暴露，就讓最後船改泊並把帳證拆開離港。
- 資源：貨棧、腳夫、兩名可信船戶、現銀、潮時知識、已發出的付款與船戶安排。
- 限制：不能控制海關或蒼龍門；每次假簿仍需真貨補數；被捕／死亡不會讓已發出的命令憑空取消，也不能讓他再親自指揮。
- 改變計畫條件：`broker_alert=high` 時拆證／換船；`final_ship=detained` 時放棄靠船運出副頁；`ledger_chain=strong` 且本人自由時優先處理帳證而非保貨。
- 可預見反應：被查帳就切斷帳房接口；一船被扣則犧牲該船保另一艘；本人被捕／死亡時，由既定船戶與已付款燈役繼續到看見正式停航或自身風險改變為止。

### `actor_clerk` — `<NPC#1@戰役:斷潮三簿: 姓?-名?>`
- 身份／位置：海關轉倉書吏；第一本簿的直接責任人。
- 初始知道：自己改過的時刻、收款與指定船號；知道 `<NPC#2>` 是付款來源。
- 初始不知道／誤解：不知道舊印放線、錯燈、最終收貨全貌；起初把事情理解成逃稅插隊。
- 核心利益：保住家計、避免替 `<NPC#2>` 扛下全部責任，也希望停止再被利用。
- 當前計畫：把本次爭議改寫成「七、九船號抄反」。
- 資源：草頁、值房簿冊知識、前三次改時刻記憶。
- 限制：不能改碼頭實際進出、倉戶時刻與船體吃水；若被拘押、逃走或死亡，後篇不能假裝其本人仍可作證。
- 改變計畫條件：兩項獨立物證並有依法記錄其有限責任時轉為合作；被正式拘押後由封存簿冊替代其現場功能。
- 可預見反應：合作時提供自己改過的時刻與船號；逃亡／死亡時只保留筆跡、草頁、倉戶時刻等已成立物證，不產生新的口供。

### `actor_deputy` — `<NPC#3@戰役:斷潮三簿: 姓?-名?>`
- 身份／位置：海關巡驗副手。
- 初始知道：吃水矛盾、自己越權私留舊印、曾用舊印放線。
- 初始不知道／誤解：不知道 `<NPC#4>` 身份與錯燈細節；誤判引航端存在穩定內應網。
- 核心利益：抓完整責任鏈，同時避免越權行為令自己失職。
- 當前計畫：讓可疑船再以舊印過驗，暗跟到收貨端。
- 資源：巡驗職務、兩名知道部分放線安排的差役、舊印與驗牒記錄。
- 限制：沒有正式密令；舊印曝光會損害職位與證據可信度；失去職權後不能繼續主辦扣船。
- 改變計畫條件：`deputy_sting=stopped` 時交印並停止放線；`exposed` 時退出主辦；死亡／失蹤時由印匣領用簿與差役記錄承接最低必要資訊。
- 可預見反應：證據不足時反對全面扣港；證據充分時接受合法扣查；被揭露越權後不會復權或偷偷重新取得舊印。

### `actor_lamplighter` — `<NPC#4@戰役:斷潮三簿: 姓?-名?>`
- 身份／位置：普通夜間燈役；第3篇開始成為跨篇具體人物，第4篇直接處理。
- 初始知道：有人付3兩、指定夜潮、指定第三燈與「候驗改可入內灣」要求。
- 初始不知道／誤解：不知道三簿、舊印與走私全貌；誤以為只讓熟船少等一次查驗，不會害人。
- 核心利益：償債、保差事；知道會危及普通船後，避免害人與自保優先於3兩。
- 當前計畫：試燈後借故獨自登第三燈礁換遮片，潮後換回。
- 資源：合法輪值身分、第三燈接觸權、已藏備用遮片。
- 限制：不能調動蒼龍門、不能改其他四燈、不能命令船隻；被拘押／死亡後不能再親自執行錯燈。
- 改變計畫條件：`lamp_link=identified` 時警覺並可能請假／換班；被正式拘押則錯燈本人路線消失；看到普通船將受害時可被說服停手。
- 可預見反應：面臨付款＋輪值互證時交遮片與指定船；提前死亡／拘押時，遮片、付款、輪值、跑腿描述仍只證其個人受賄，不把責任擴張到整個引航制度。

### `actor_pilot_service` — 海陵引航值棚／蒼龍灣引航制度
- 身份／位置：制度性行動者，不是單一 NPC，不分配戰役 NPC key。
- 初始知道：正常燈號、輪值、航道安全規範；不知道貨棧三簿走私全貌。
- 核心利益：航道安全與燈號可信，避免單一燈役過錯被誤認為整個制度共謀。
- 當前計畫：維持正常輪值；有正式異常時更換燈役並要求可核查證據。
- 資源：值棚輪值表、燈號規範、普通引航人與對燈具的制度控制。
- 限制：不掌握貨棧帳證與海關私留舊印的內情。
- 改變計畫條件：`pilot_trust=cooperative` 時先提供合法抄副與協助處燈；`hostile` 時要求正式公文，但不得讓必要公開資料消失。
- 可預見反應：被無證公開歸責時收緊合作；玩家明確區分個人與制度責任時維持或提高合作。

## 四、戰役級 NPC registry
| key | 姓名欄 | 跨篇功能 | actor_key | 首次規劃登場 | 首次正式登場／`script_id` | 來源／alias |
|---|---|---|---|---|---|---|
| `NPC#1@戰役:斷潮三簿` | `姓?-名?` | 海關轉倉書吏；第一本簿入口 | `actor_clerk` | 第1篇 | 第1篇／`ootb_campaign_broken_tide_s1_early_ledger_v1` | 無 |
| `NPC#2@戰役:斷潮三簿` | `姓?-名?` | 船盟外包貨棧掌櫃；主要組織者 | `actor_shipbroker` | 第1篇 | 第1篇／`ootb_campaign_broken_tide_s1_early_ledger_v1` | 無 |
| `NPC#3@戰役:斷潮三簿` | `姓?-名?` | 海關巡驗副手；越權放線者 | `actor_deputy` | 第1篇 | 第1篇／`ootb_campaign_broken_tide_s1_early_ledger_v1` | 無 |
| `NPC#4@戰役:斷潮三簿` | `姓?-名?` | 普通夜間燈役；錯燈執行者 | `actor_lamplighter` | 第3篇 | 第3篇／`ootb_campaign_broken_tide_s3_old_seal_v1` | 無 |

編號永久保留；死亡、退出、拘押或未來增修都不得重用。任何新增跨篇具體人物必須先在本表取得新 key，再進未發布階段。

## 五、campaign state registry
| `state_key` | 型別／可用值 | 初始值 | 首次建立來源 | 代表的世界事實 | 後續讀取與實際效果 |
|---|---|---|---|---|---|
| `ledger_chain` | `none / partial / strong` | `none` | 第1篇 | 三本簿及替代證據的互證強度 | 第2–4篇決定責任鏈可達強度與末篇 ending 上限；證物毀損可降級，不得憑猜測升級 |
| `clerk_status` | `free / cooperating / detained / fled / dead` | `free` | 第1篇 | `<NPC#1>` 是否可親自作證／提供草頁 | 第2–4篇決定本人是否可用；非可用狀態改讀封存簿冊、筆跡、倉戶時刻 |
| `broker_alert` | `low / high` | `low` | 第1篇 | `<NPC#2>` 是否已察覺調查逼近 | 第2–4篇改船號、帳證位置、撤離時機；不刪除已成立的潮時／付款痕跡 |
| `deputy_sting` | `active / stopped / exposed` | `active` | 第1篇 | `<NPC#3>` 私留舊印放線是否仍在運作 | 第2–4篇決定其是否仍主辦、舊印如何處置及誰能依法扣船 |
| `old_seal_secured` | bool | `false` | 第3篇 | 舊印實物是否依法封存 | 第4篇影響責任鏈強度；false 時只能靠領用簿＋差役證詞處理越權 |
| `lamp_link` | `unknown / suspected / identified` | `unknown` | 第3篇 | `<NPC#4>` 與付款／輪值的接口強度 | 第4篇決定能否提前定位燈役；identified 也可能令其請假／換班 |
| `final_ship` | `scheduled / rerouted / detained / sailed` | `scheduled` | 第2篇 | 最後船與最後副頁的實際位置／控制狀態 | 第3–4篇選擇原船、備用船、已扣船或岸上證據路線；不得重置成 scheduled |
| `pilot_trust` | `neutral / cooperative / hostile` | `neutral` | 第3篇 | 引航值棚對玩家查驗的合作程度 | 第4篇影響抄副、公文與處燈合作；hostile 只增加合法程序，不刪必要資料 |
| `campaign_status` | `active / partly_completed / failed / completed` | `active` | 戰役開始 | 本桌戰役是否可繼續、已提早收束或完整收束 | 每篇正式結算必寫；只有 active 且目標篇解鎖路線成立才能宣告下一篇 |
| `campaign_progress` | `0/4 / 1/4 / 2/4 / 3/4 / 4/4` | `0/4` | 戰役開始 | 已正式結算到的最高階段 | 每篇正式 ending 結算後更新為該篇序號；只作進度記錄，不單獨構成下一篇解鎖 |

承接裁決固定在**前一階段正式結算**：GM 以該次 `campaign_save` 與本篇 frozen ending/state 核對下列完整路線，成立才把「已解鎖的目標階段＋匹配路線」寫入新版 `campaign_save`。下一次開局只載入該裁決，不重新計算。

## 六、階段接口、解鎖路線與 ending 映射

### 第1篇《潮倉三本簿有一本總比貨早到》
- 狀態：正式完成。
- `script_id`：`ootb_campaign_broken_tide_s1_early_ledger_v1`
- 正式檔名：`OOTB_戰役任務_斷潮三簿(1)_潮倉三本簿有一本總比貨早到.md`
- 帶入 state：總綱初始 `ledger_chain=none`、`clerk_status=free`、`broker_alert=low`、`deputy_sting=active`、`campaign_status=active`、`campaign_progress=0/4`。
- 直接使用戰役 NPC：`NPC#1`、`NPC#2`、`NPC#3`。
- 為甚麼現在：潮門絞軸故障令本應補數的真貨船延誤，已提前寫入的臨簿第一次在貨未到時暴露。
- 為甚麼玩家：海關值房不願停掉整排潮倉，給外查角色一天核對爭議簿與缺貨去向。
- 可獨立完成目標：查清本次「簿早於貨」的直接原因並處理缺貨／偽簿責任。
- 局部真相：`<NPC#1>` 依 `<NPC#2>` 船號提前填臨簿，青尾九號原要用真貨補青尾七號的帳面缺口；`<NPC#3>` 想把事情壓成抄錯以維持自己的上游放線。
- 與跨篇真相接觸：第一次固定「提前臨簿＋船號補數」方法及 `<NPC#2>` 的貨棧接口，但不要求玩家知道舊印與錯燈。
- 可改變 state：`ledger_chain`、`clerk_status`、`broker_alert`、`campaign_status`、`campaign_progress`。
- 本篇完成後：任何 ending 都完成眼前臨簿／缺貨事件；只有仍保留正式查驗接口的兩個 ending 可在本篇結算時解鎖第2篇。

Ending 映射：
- `bt1_documented`：`ledger_chain=partial`；`clerk_status` 按當場處置為 `cooperating / detained / free`；秘密交證且未驚動貨棧時 `broker_alert=low`，否則 `high`；`deputy_sting` 保持實值（通常 `active`）；**可承接 → 第2篇路線 S2-A**；`campaign_status=active`、`campaign_progress=1/4`。
- `bt1_clerk_only`：`clerk_status=detained`、`ledger_chain=none`、`broker_alert=high`、`deputy_sting` 保持實值；海關複核自然產生新量水矛盾；**可承接 → 第2篇路線 S2-B**；`campaign_status=active`、`campaign_progress=1/4`。
- `bt1_false_clean`：**提早戰役結局／部分完成**；`campaign_status=partly_completed`、`campaign_progress=1/4`。已回答：本次缺貨與行政責任；未回答：重複船號、上游貨棧與後續三簿鏈。關鍵 NPC／證物按本篇實際保存，沒有可追的正式接口；原定第2篇不再由本案啟動。玩家可見收束沿階段正文《一頁歸檔》，宣讀後宣告「戰役部分完成（1/4）」；最後的重複貨號傳聞只作不劇透謎面尾巴，不是新委託。
- `bt1_abandon`：**提早戰役結局／失敗**；`campaign_status=failed`、`campaign_progress=1/4`。保存角色退出、證物與 NPC 當時狀態；原定第2篇不得自動承接。

### 第2篇《兩艘空船都報了滿艙吃水》
- 狀態：正式完成。
- `script_id`：`ootb_campaign_broken_tide_s2_false_draft_v1`
- 正式檔名：`OOTB_戰役任務_斷潮三簿(2)_兩艘空船都報了滿艙吃水.md`
- 帶入 state：第1篇已結算的 `ledger_chain`、`clerk_status`、`broker_alert`、`deputy_sting`、`campaign_status`、`campaign_progress`，以及三名戰役 NPC 與玩家／官署持有證物的實際狀態；`final_ship` 尚未被前篇改寫時按初始 `scheduled`。
- 直接使用戰役 NPC：`NPC#2`、`NPC#3`；`NPC#1` 狀態只從 `campaign_save` 讀取，非必要出場。
- 為甚麼現在：第1篇結算後海關複核量水紙，發現兩艘近期「滿艙」船的吃水互相矛盾；夜潮四小時後會讓其中一艘離泊。
- 為甚麼玩家：玩家已是第1篇正式外查人，且本次矛盾正由其已結算案卷／複核產生，海關直接續委託。
- 可獨立完成目標：核定實際船體、貨量與搬運鏈，完成本批船貨的扣驗／處置。
- 局部真相：青尾七號是空殼船號，青尾九號載真貨；海鷺二號再接走同批貨一半，讓兩本載貨簿都顯得有貨。
- 與跨篇真相接觸：固定第二本簿的船號補數方法，並讓 `<NPC#2>` 的警覺與最後船位置開始受玩家結果影響。
- 可改變 state：`ledger_chain`、`broker_alert`、`final_ship`、`campaign_status`、`campaign_progress`；保留第1篇所有仍有效人物／證物狀態。

完整解鎖路線：
- **S2-A**：`bt1_documented AND campaign_status=active`。來源：第1篇正式 ending；帶入其 `ledger_chain/clerk_status/broker_alert` 差異。
- **S2-B**：`bt1_clerk_only AND campaign_status=active`。來源：第1篇正式 ending；即使 `ledger_chain=none`，海關對被拘書吏案卷的複核仍足以發現量水矛盾。
- 其他第1篇 ending 均沒有合法路線；第2篇保持鎖定。

Ending 映射：
- `bt2_chain`：`ledger_chain=strong`；`final_ship=scheduled`；`clerk_status`、`broker_alert`、`deputy_sting` 保留進篇實值（後續只按正式反應規則變動）；**可承接 → 第3篇路線 S3-A**；`campaign_status=active`、`campaign_progress=2/4`。
- `bt2_stop_cargo`：`ledger_chain=partial`、`broker_alert=high`、`final_ship=rerouted`；`clerk_status/deputy_sting` 保留實值；**可承接 → 第3篇路線 S3-B**；`campaign_status=active`、`campaign_progress=2/4`。
- `bt2_wrong_ship`：**提早戰役結局／部分完成**；`campaign_status=partly_completed`、`campaign_progress=2/4`。已回答：眼前錯船與扣船爭議；未回答：真貨去向、舊印與燈役。真正貨與帳證已轉移且沒有留下可追舊印／貨棧接口，因此第3篇不再由本案啟動。人物、船貨、證物按實際保存。玩家可見收束沿《空艙有主》，宣讀後宣告「戰役部分完成（2/4）」；夜潮後的無主貨消息只作謎面尾巴。
- `bt2_abandon`：**提早戰役結局／失敗**；`campaign_status=failed`、`campaign_progress=2/4`；保存當時船貨／人物／證物狀態，第3篇不得自動承接。

### 第3篇《海陵三道驗牒有一道只認舊印》
- 狀態：正式完成。
- `script_id`：`ootb_campaign_broken_tide_s3_old_seal_v1`
- 正式檔名：`OOTB_戰役任務_斷潮三簿(3)_海陵三道驗牒有一道只認舊印.md`
- 帶入 state：此前所有仍有效的 `ledger_chain`、`clerk_status`、`broker_alert`、`deputy_sting`、`final_ship`、`campaign_status`、`campaign_progress`，以及戰役 NPC、船貨、載貨副頁與其他已保存證物狀態。
- 直接使用戰役 NPC：`NPC#2`、`NPC#3`、`NPC#4`；`NPC#1` 只依前史狀態提供本人或替代物證。
- 為甚麼現在：第2篇扣貨／船貨記錄中出現半年前已停用的真舊驗印，而下一夜班三小時後接手；`<NPC#3>` 的越權放線正要失控。
- 為甚麼玩家：第2篇正式扣驗案卷直接把舊印矛盾交給同一外查隊，且玩家已掌握可核查的船貨前史。
- 可獨立完成目標：查明舊印來源與當夜驗牒責任，處理越權放線及單一燈役接口。
- 局部真相：舊印由 `<NPC#3>` 私留作未授權放線；`<NPC#2>` 已察覺並故意留下舊印牒嫁禍，同時已支付 `<NPC#4>` 錯燈訂金。
- 與跨篇真相接觸：第三本簿固定「海關越權但非走私內應」；同時把燈役責任限制為具體個人，避免把蒼龍門／整個引航制度誤寫成共謀。
- 可改變 state：`deputy_sting`、`old_seal_secured`、`lamp_link`、`pilot_trust`、`broker_alert`、`final_ship`、`campaign_status`、`campaign_progress`；保留所有更早仍有效 state。

完整解鎖路線：
- **S3-A**：`bt2_chain AND campaign_status=active`。來源：第2篇；第1篇留下的 `clerk_status/broker_alert` 與證物狀態照存，但不作額外門檻。
- **S3-B**：`bt2_stop_cargo AND campaign_status=active`。來源：第2篇；同時必帶入其 `ledger_chain=partial`、`broker_alert=high`、`final_ship=rerouted`。
- 第1篇因素若仍有效，作本篇證據／人物差異，不另組成缺一不可的 AND 門檻；其差異不得被洗平。
- 其他第2篇 ending 均沒有合法路線；第3篇保持鎖定。

Ending 映射：
- `bt3_sting_stopped`：`deputy_sting=stopped`；舊印實物依法封存則 `old_seal_secured=true`，實物失去則 `false`；付款＋輪值兩類互證則 `lamp_link=identified`，只有一類則 `suspected`，皆無則 `unknown`；`pilot_trust` 按本篇實際互動為 `cooperative / neutral`（若無證泛化歸責致接口失去，改走 `bt3_blame_pilots`）；`broker_alert/final_ship` 保留進篇實值；**可承接 → 第4篇路線 S4-A**；`campaign_status=active`、`campaign_progress=3/4`。
- `bt3_sting_exposed`：`deputy_sting=exposed`、`broker_alert=high`、`final_ship=rerouted`；`old_seal_secured` 依實物是否依法封存；`lamp_link` 仍依付款／輪值證據為 `unknown / suspected / identified`；未泛化指控時 `pilot_trust=cooperative`，若接口被泛化歸責破壞則不得用本 ending 承接而改走 `bt3_blame_pilots`；**可承接 → 第4篇路線 S4-B**；`campaign_status=active`、`campaign_progress=3/4`。
- `bt3_blame_pilots`：**提早戰役結局／部分完成**；`pilot_trust=hostile`、`lamp_link=unknown`、`campaign_status=partly_completed`、`campaign_progress=3/4`。已回答：舊印來源與越權責任；未回答：單一燈役及最後船完整責任鏈。因泛化歸責令引航端接口失去，原定第4篇不再由本案啟動。玩家可見收束沿《舊印入匣》，宣讀後宣告「戰役部分完成（3/4）」；「一班燈役被撤但外人不知原因」作最後謎面尾巴，不是新委託。
- `bt3_abandon`：**提早戰役結局／失敗**；`campaign_status=failed`、`campaign_progress=3/4`；保存舊印、輪值、人物當時狀態，第4篇不得自動承接。

### 第4篇《定潮島外五盞引航燈有一盞不照船》
- 狀態：正式完成；末篇。
- `script_id`：`ootb_campaign_broken_tide_s4_false_lamp_v1`
- 正式檔名：`OOTB_戰役任務_斷潮三簿(4)_定潮島外五盞引航燈有一盞不照船.md`
- 帶入 state：此前全部仍有效的 `ledger_chain`、`clerk_status`、`broker_alert`、`deputy_sting`、`old_seal_secured`、`lamp_link`、`final_ship`、`pilot_trust`、`campaign_status`、`campaign_progress`，以及四名戰役 NPC、舊印、輪值／付款證據、最後船與玩家持有物的實際狀態。
- 直接使用戰役 NPC：`NPC#2`、`NPC#3`、`NPC#4`；`NPC#1` 僅按前史狀態提供本人或替代物證。
- 為甚麼現在：`<NPC#2>` 在第3篇前已支付錯燈訂金；指定夜潮三小時內到來，第三燈的錯號安排與最後船／岸上副頁即將同時生效。
- 為甚麼玩家：第3篇正式結算已把單一燈役／輪值接口交給同一查驗隊，並在該次結算宣告末篇解鎖；玩家不是靠新委託重新進場。
- 可獨立完成目標：保護航道、處理錯燈與最後船／岸上代用品，固定能成立的最終責任鏈。
- 局部真相：`<NPC#4>` 只收一次性3兩訂金，按指定夜潮改第三燈；最後船攜未完稅貨及能把貨棧支出與船號連起來的收貨暗記副頁。
- 與跨篇真相接觸：直接處理錯燈、最後船與前三本簿能否合成完整責任鏈；沒有再把核心答案推往第5篇。
- 可改變 state：所有仍有效 state 的末值、`campaign_status`、`campaign_progress`，以及最後副頁取得／留置／失落的 `campaign_save` 例外。

完整解鎖路線：
- **S4-A**：`bt3_sting_stopped AND campaign_status=active`。來源：第3篇；並帶入此前全部仍有效 `ledger_chain/clerk_status/broker_alert/final_ship/old_seal_secured/lamp_link/pilot_trust`。
- **S4-B**：`bt3_sting_exposed AND campaign_status=active`。來源：第3篇；同樣帶入更早全部仍有效 state，尤其 `broker_alert=high`、`final_ship=rerouted`。
- 早期 state 不再作額外「有／無」門檻，但必須實際改變末篇船、證據、人物與合作路線；不得洗平成單一標準開場。
- 其他第3篇 ending 均沒有合法路線；末篇保持鎖定。

Ending 映射：
- `bt4_chain_closed`：責任鏈完整，`campaign_status=completed`、`campaign_progress=4/4`；戰役完整成功收束。
- `bt4_harbor_saved`：航道與當前危機解決但責任鏈 partial；`campaign_status=completed`、`campaign_progress=4/4`；原定四篇已跑至末篇，未證明部分留作世界未知，不新增第5篇。
- `bt4_false_signal`：錯燈一度成功但人船／部分責任仍被救回或固定；`campaign_status=completed`、`campaign_progress=4/4`；屬末篇正式失敗但有收束，因原定路線已完成，不映射為 `failed`。
- `bt4_abandon`：玩家正式退出核心事件；`campaign_status=failed`、`campaign_progress=4/4`；保存所有末值與最後副頁狀態，不新增第5篇。
- 末篇每個 ending 都以階段正文的玩家可見收束當場結算，之後世界可有追責、追船、制度整改，但不自動建立下一階段。

## 七、條件式反應
- `broker_alert=high`：`<NPC#2>` 提前拆帳證、改最後船號；潮時與付款痕跡不消失。
- `clerk_status=cooperating`：`<NPC#1>` 可提供自己實際改過的時刻與船號；仍需物證互證。
- `clerk_status=detained`：海關封存簿冊，以封存副本替代本人出場。
- `clerk_status=fled/dead`：只讀筆跡、草頁、倉戶時刻等已成立來源，不生成新口供。
- `deputy_sting=active`：`<NPC#3>` 繼續舊印放線，直到第三篇處理。
- `deputy_sting=stopped`：交印並停止私線；若末篇仍在職，只可用合法權限協助。
- `deputy_sting=exposed`：失去主辦權，既有證詞／差役記錄仍可用；普通值房接手合法扣船。
- `pilot_trust=hostile`：引航端要求正式公文；不刪除必要資料，只增加合法取得時間。
- `lamp_link=identified`：`<NPC#4>` 可能請假／換班；付款、輪值與遮片痕跡仍存在。
- `<NPC#4>` 提前拘押／死亡：錯燈不再由其本人執行；末篇仍需處理已藏遮片、最後船與航道安全，但不得補造第二名內應。

## 八、跨篇關鍵依賴與回歸代用品

### 關鍵人物
| 依賴 | 可能例外 | 正式回歸／收束 |
|---|---|---|
| `<NPC#1>` 的改簿知識 | 死亡、逃走、拘押、不合作 | 草頁／筆跡＋倉戶時刻固定其局部責任；後篇只失去口供強度，不失去船號／時間矛盾 |
| `<NPC#2>` 的組織角色 | 提前被捕、死亡、合作 | 已發出的船戶、貨棧支出、付款與最後船安排依 frozen state 繼續；本人不越獄／復活，若主因果已被玩家真正解除則依當篇 ending 提早收束或降低末篇責任鏈 |
| `<NPC#3>` 的放線／官職 | 死亡、失蹤、停職、曝光 | 舊印、印匣領用簿、兩名差役記錄承接越權事實；失權後由普通值房執行合法扣船，不繼承其私人誤判 |
| `<NPC#4>` 的錯燈執行 | 提前拘押、死亡、倒戈、合作 | 不生成替身內應；錯燈本人路線消失，已藏遮片、付款、輪值、跑腿描述仍固定其已成立受賄，末篇轉重航道安全與最後船／責任鏈 |

### 關鍵物品／證物
- 轉倉臨簿毀損：倉戶簽收時刻＋值房抄副互證；兩者同失才降低 `ledger_chain`。
- 載貨簿毀損：碼頭量水尺＋兩名不同班次裝卸人的貨量記憶互證；單一口供不能升 `strong`。
- 舊驗印丟失／毀損：印匣領用簿＋兩名差役證詞仍可證越權，但失去精細印痕比對，`old_seal_secured=false`。
- 燈役付款證物失去：貨棧支出副頁＋輪值交換／跑腿描述互證；錢袋不是唯一來源。
- 最後收貨暗記副頁失去：末篇仍可保航道並以三簿＋岸上付款／輪值固定 partial 責任，最高只能走相應較弱 ending，不補造完美副本。
- 玩家帶走／公開上述證物：保存實際持有人與公開程度；後篇改用玩家持有原件或依法取得副本，不假定證物仍在原處。

### 必要世界條件
- 海關值房／合法扣驗權：`<NPC#3>` 失權不等於海關消失；由普通值房依既有案卷執行職務權限，但不繼承其私人知識。
- 引航值棚／第三燈：`pilot_trust=hostile` 只改為正式公文路線；若 `<NPC#4>` 已不可用，制度仍能提供正常燈號與航道安全資料。
- 最後船狀態：
  - `scheduled`：原定海鷺九候潮；
  - `rerouted`：改至青篷二十七；
  - `detained`：船與副頁已受控，末篇改保護航道與固定責任；
  - `sailed`：不保證追回，改用岸上證據處理較弱責任鏈，世界另行追船。
  以上值一經前篇結算不得重置。

## 九、提早戰役結局保存要求
所有非末篇不可承接 ending 都在相應階段當場形成正式戰役結局，不把「後篇開不了」留給下一次開局處理。除下列 ending 明列覆寫的 `campaign_status/campaign_progress` 與其他 state 外，其餘 campaign state、戰役 NPC、關鍵物品／證物、持有人、公開程度與世界條件一律凍結為該篇正式結算時的實值並寫入 `campaign_save`；戰役收束後不再由未發生的後篇改動。

- `bt1_false_clean`：`partly_completed`、1/4；保存三名已登場戰役 NPC、臨簿／草頁／貨物當時狀態及沒有正式可追接口的事實；宣告「戰役部分完成（1/4）」。
- `bt2_wrong_ship`：`partly_completed`、2/4；保存船貨、`ledger_chain`、人物與已失去的舊印／貨棧接口；宣告「戰役部分完成（2/4）」。
- `bt3_blame_pilots`：`partly_completed`、3/4；保存 `pilot_trust=hostile`、`lamp_link=unknown`、舊印與人物狀態；宣告「戰役部分完成（3/4）」。
- `bt1_abandon / bt2_abandon / bt3_abandon`：各自 `failed` 並停於 1/4、2/4、3/4；保存角色退出與當時所有已成立後果，不提供回歸主線。
- 每個 `partly_completed` 玩家可見收束以相應階段正文為權威：先完成眼前案件與直接後果，最後才留不劇透謎面尾巴；尾巴不得變成新委託、追擊令或「真正任務才開始」。

## 十、不得 retcon
1. 第1篇確定 `<NPC#1>` 偽造本次臨簿；後篇不得改成完全無責。
2. 第2篇確定空船號／真貨船交換；後篇只補誰利用及為何。
3. 第3篇舊印確由 `<NPC#3>` 越權私留；後篇不得改成 `<NPC#2>` 偽造同印。
4. 第4篇只有單一燈役受賄；不得升格成蒼龍門或整個引航制度參與走私。
5. 玩家造成的死亡、扣船、公開揭露、證物持有與其他例外由 `campaign_save` 保存；後篇依 state 改場景，不回寫本檔假裝原本如此。
6. 前一篇正式結算已宣告的「可承接／提早收束」不得在下一次開局因新版總綱而重算或推翻。

## 十一、擴張安全邊界
本版本戰役已完結，沒有預設第5篇。若日後另作擴張：
- 不推翻四篇已發布局部真相、ending、NPC identity 或 `campaign_save`；
- 不重置既有 state，不重編／重用 `NPC#1–4@戰役:斷潮三簿`；
- 新跨篇具體人物先進本 registry；
- 新篇只能由既有世界後果或新成立的人物反應接出，不能把既有 `partly_completed/failed` 追溯改寫成其實未中斷；
- 若插入尚未被某桌結算的新路線，重新計算受影響的未來解鎖接口並保留更早仍有效來源；
- 已結算桌次只讀其已宣告承接／收束，不用 repository 新版本回算歷史。

## 十二、戰役完成與保存
原定四篇全部完成。前三篇的不可承接 ending 已各自在當篇形成 `partly_completed` 或 `failed` 提早戰役結局；放棄一律終止。第4篇是唯一原定末篇，所有非放棄 ending 均在原定完整路線上正式收束為 `completed`，放棄為 `failed`。

末篇正式結算保存：
- 第4篇 `ending_id`；
- `campaign_status`、`campaign_progress=4/4`；
- 全部仍有效 state 的末值；
- 四名戰役 NPC 的實例姓名與最終狀態；
- 最後收貨暗記副頁的取得／留置／失落；
- 玩家仍持有或已交付的關鍵證物及公開程度；
- 任何合理例外與其世界後果。

世界仍可有追責、追船、制度整改與人物後續，但不自動新增第五篇。只有本總綱獨立通過 `戰役總劇本檢查.md`、四篇維持各自 Phase B 通過，且本總綱＋四篇最終 md 一起通過 `戰役整體覆檢.md`，才可把完整戰役整合至 `main`。
