# OOTB 戰役總劇本：折烽四牒

## 規格頭
- 戰役名：折烽四牒
- `campaign_id`：`ootb_campaign_broken_beacon_four_dispatches_v1`
- 總劇本版本：1.1.0
- 戰役狀態：連載中
- 規劃階段：4；目前正式階段：3／4。
- 共同起點：劍南道北緣山驛、關道與軍民共用烽遞線。
- 走向：第1篇4–7級中型；第2篇5–8級中型；第3篇6–9級大型；第4篇7–10級大型。
- repository 只保存作者權威；單桌姓名、傷亡、證物持有與已宣告路線存 `campaign_save`。

### 正式／規劃階段
|序|篇名|script_id|正式檔名|狀態|
|---|---|---|---|---|
|1|山驛四封急牒有一封比馬早到|`ootb_campaign_broken_beacon_s1_early_dispatch_v1`|`OOTB_戰役任務_折烽四牒(1)_山驛四封急牒有一封比馬早到.md`|已完成|
|2|兩輛急運車都掛著同一塊載貨牌|`ootb_campaign_broken_beacon_s2_duplicate_load_v1`|`OOTB_戰役任務_折烽四牒(2)_兩輛急運車都掛著同一塊載貨牌.md`|已完成|
|3|三座烽臺有一座總慢半刻|`ootb_campaign_broken_beacon_s3_late_beacon_v1`|`OOTB_戰役任務_折烽四牒(3)_三座烽臺有一座總慢半刻.md`|已完成|
|4|山口兩道封牒只剩一道還算數|`ootb_campaign_broken_beacon_s4_last_pass_v1`|`OOTB_戰役任務_折烽四牒(4)_山口兩道封牒只剩一道還算數.md`|規劃中|

## 跨篇核心答案與既存因果
北線轉運承辦 `<NPC#2@戰役:折烽四牒: 姓?-名?>` 利用驛牒與關卡兩套時鐘，把未驗商貨夾入合法急運車。驛丞 `<NPC#1@戰役:折烽四牒: 姓?-名?>` 由補缺馬班次演變成收錢提前蓋時刻。巡烽校尉 `<NPC#3@戰役:折烽四牒: 姓?-名?>` 察覺矛盾後越權延後一座烽臺點火，想放線跟車；他不是走私同夥。承辦察覺被追後買通山口繩橋管事 `<NPC#4@戰役:折烽四牒: 姓?-名?>`，要求末篇把封道牌晚掛半刻。

四牒依次為驛站急牒、車隊載貨牒、烽臺值更牒、山口封道牒。戰役開始前：NPC#1 已預蓋三次；NPC#2 已夾貨兩次並安排最後批次；NPC#3 已越權延火一次；NPC#4 已收2兩訂金但未動橋。玩家介入後誰被捕、合作、死亡，證物與最後貨去向均由 ending/state 決定。無玩家時前三項責任會互相遮蔽，最後帳牒越山口後制度雖封，完整責任鏈難證。

## actor 與 NPC registry
- `actor_postmaster`＝NPC#1：山驛驛丞；知道預蓋、付款來源，不知烽臺／山口；利益為保職與避免替罪；兩項獨立證據後合作；本人失效由印簿、換馬牌、值房副簿承接。
- `actor_carrier`＝NPC#2：轉運承辦；知道夾貨方法、最後批次，不知校尉完整放線；利益為承辦權與可切割性；`carrier_alert=high` 拆帳牒，`last_load=detained` 放貨保帳；本人失效不取消既發車令。
- `actor_beacon`＝NPC#3：巡烽校尉；知道吃重矛盾與自己越權延火，誤判山口有長期內應；利益為抓完整鏈並保職；`beacon_sting=stopped` 交牒，`exposed` 退出主辦；本人失效由值更牒與兩烽卒承接。
- `actor_bridge`＝NPC#4：山口繩橋管事；只知收錢晚掛封道牌，不知前三篇全貌；利益為還債且不背軍務重罪；見正式封道令或付款者已捕會動搖；本人失效由訂金包封、橋務副簿、接頭腳夫承接。

戰役 NPC key 唯一為上述 NPC#1–#4，姓名約束均 `姓?-名?`；首次正式登場依次為第1、第1、第2、第3篇。

## campaign state
`dispatch_chain=none/partial/strong`（初始none）；`postmaster_status=free/cooperative/detained/gone`（free）；`carrier_alert=low/high`（low）；`beacon_sting=active/stopped/exposed`（active）；`bridge_status=normal/compromised/secured`（normal）；`last_load=planned/rerouted/detained/escaped`（planned）；`campaign_status=active/partly_completed/failed/completed`（active）；`campaign_progress` 初始0/4。

## 階段接口
### 1 山驛四封急牒有一封比馬早到
帶入初始 state；NPC#1、#2。現在發生：第四封牒蓋印早於真馬到站。玩家介入：值房需外查人在下一班車前核對。目標：查時刻、保牒證、處理出車。局部真相：NPC#1 預蓋，NPC#2 原擬用真牒補平。跨篇接觸：同車號在兩套時鐘不一致。輸出：`dispatch_chain/postmaster_status/carrier_alert`。
- `s1_chain_open`：partial、high、active、1/4 → 第2篇。
- `s1_quiet_proof`：partial、low、active、1/4 → 第2篇。
- `s1_false_close`：none、partly_completed、1/4 → 提早收束《驛簿已封》；眼前錯簿結案，無合法車隊接口，後續 state 凍結，已成立人物／證物保存。
- `s1_abandon`：failed、1/4，終止。

### 2 兩輛急運車都掛著同一塊載貨牌
解鎖只在第1篇結算判定：`s1_chain_open OR s1_quiet_proof`。帶入 partial、`carrier_alert/postmaster_status`；NPC#2、#3。現在發生：同車號兩車同時過不同關。玩家介入：前篇已取得車號接口。目標：分真急運與夾貨車。局部真相：NPC#2 輪換合法牌夾貨；NPC#3 暗中放其中一車。跨篇接觸：吃重與時刻連到烽牒。輸出：`dispatch_chain/beacon_sting/carrier_alert`。
- `s2_two_clocks`：strong、active、2/4 → 第3篇。
- `s2_load_only`：partial、active、2/4 → 第3篇。
- `s2_wrong_master`：partly_completed、2/4 → 提早收束《扣住了車，斷了線》；兩車危機收住，真正車隊接口因正式錯判而失去，後續凍結。
- `s2_abandon`：failed、2/4。

### 3 三座烽臺有一座總慢半刻
解鎖只在第2篇結算判定：`s2_two_clocks OR s2_load_only`；另載入第1篇已保存 `carrier_alert`，不重算舊 ending。帶入 `dispatch_chain/carrier_alert/beacon_sting`；NPC#2、#3、#4。現在發生：第三臺三次慢半刻，末批貨同夜要過封道。玩家介入：已有合法查車／牒證接口。目標：查延火、處理放線、保封道。局部真相：NPC#3 越權延火；NPC#2 察覺後另買通 NPC#4，兩者無共謀。輸出：`beacon_sting/bridge_status/last_load/dispatch_chain`。
- `s3_split_fault`：bridge compromised、last_load rerouted、active、3/4 → 第4篇。
- `s3_secure_road`：bridge secured、last_load detained、active、3/4 → 第4篇，由追收責任／帳牒開始。
- `s3_blame_beacon`：partly_completed、3/4 → 提早收束《烽火復明，山口無證》；烽臺恢復、山口責任鏈失去合法證據，後續凍結。
- `s3_abandon`：failed、3/4。

### 4 山口兩道封牒只剩一道還算數
解鎖只在第3篇結算判定：`s3_split_fault OR s3_secure_road`；載入既存 `dispatch_chain/carrier_alert/bridge_status/last_load` 及 NPC#2、#4 狀態。現在發生：最後帳牒與貨已分路，封道命令只有一次有效窗口。玩家介入：前三篇已建立合法山口接口。目標：處理最後貨、帳牒與責任鏈。局部真相：NPC#4 只受買通晚掛牌；主要組織仍為 NPC#2，NPC#3 越權另案。末篇必須讓玩家接觸並處理四牒責任鏈；所有 ending `campaign_progress=4/4`，完整收束為 completed，封漏洞但證據不足可 partly_completed，明確放棄或最後貨與帳證皆失且無合理重建為 failed。

## 失效回歸與擴張邊界
人物失效使用 registry 已列替代來源，不生成新口供。關鍵物證毀損時只用既有獨立來源；若同一必要結論所有來源永久失去，進證據不足／失敗 ending。任何 `partly_completed` 都先結清當篇眼前危機、人物與所得，再以不揭核心答案的可見異常作尾聲；未觸發 future state 凍結。後續版本不得把 NPC#3 改成走私同夥、NPC#4 改成前三篇既有內應，亦不得推翻 NPC#1 有限補簿責任。新增階段必須先更新總綱與接口。