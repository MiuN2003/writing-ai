EXAMPLES = """Here's an example:
<example>
<input>
Opinions are divided on whether giving longer holidays to employees is a good choice to encourage them to do their jobs well. Although this action may have certain negative impacts, its benefits far outweigh them. 
Admittedly, holidays that last longer may cause some disadvantages. Firstly, employees may waste time and money on entertaining. As a result, doing so would set their goals back. In the long run, they could lose their will leading to starting over. Besides, when people have an extended holiday, their health could be affected by a sedentary lifestyle because they could drink more alcoholic drinks or consume more high-fat food during holidays, which makes people easily suffer from obesity or liver disease. Moreover, drinking and driving is very dangerous because it can easily cause traffic accidents. 
On the other hand, longer holidays offer several significant employee benefits related to family bonds and mental health. Regarding the former, holidays are the best time to enjoy and unwind with family by going on vacation, eating and watching together, or making up with parents or siblings. As a result, family members are more closed, which can strengthen family bonds. Furthermore, employees could use this time to take up new habits like attending yoga courses, reading books, or cooking, which is a key to releasing stress and improving overall well-being. Consequently, in this way, employees could easily recharge their battery life before going back to work.
In conclusion, even though there might be certain disadvantages when enjoying a longer holiday. Based on the presented arguments. I contend that its advantages are far more significant to employees.
</input>

<output>
<repair>
Opinions are divided on whether giving longer holidays to employees is a good choice to encourage them to do their jobs well. Although this action may have certain negative impacts, its benefits far outweigh them. 
Admittedly, holidays that last longer may cause some disadvantages. Firstly, employees may waste time and money on entertaining. As a result, doing so would set their goals back. In the long run, they could lose their will leading to starting over. Besides, when people have an extended holiday, their health could be affected by a sedentary lifestyle because they could drink more alcoholic drinks or consume more high-fat food during holidays, which makes people easily suffer from obesity or liver disease. Moreover, drinking and driving is very dangerous because it can easily cause traffic accidents. 
On the other hand, longer holidays offer several significant employee benefits related to family bonds and mental health. Regarding the former, holidays are the best time to enjoy and unwind with family by going on vacation, eating and watching together, or making up with parents or siblings. As a result, <span id="1" class="vocabulary">family members <s>are more closed</s><mark>become closer</mark></span>, which can strengthen family bonds. Furthermore, employees could use this time to take up new habits like attending yoga courses, reading books, or cooking, which is a key to releasing stress and improving overall well-being. Consequently, in this way, employees could easily recharge <span id="2" class="vocabulary"><s>their battery life</s><mark>themselves</mark></span> before going back to work.
In conclusion, even though there might be certain disadvantages <span id="3" class="vocabulary">when <s>enjoying</s><mark>having</mark></span> a longer holiday<span id="4" class="grammarly"><s>.</s><mark>,</mark></span> <span id="5" class="vocabulary"><s>Based on</s><mark>based on</mark></span> the presented arguments<span id="6" class="grammarly"><s>.</s><mark>,</mark></span> I contend that its advantages are far more significant to employees.
</repair>
<comment>
<explanation id="1"> "Are more closed" không phải là cách diễn đạt tự nhiên trong tiếng Anh để nói về mối quan hệ gần gũi hơn. Thay vào đó, chúng ta nên dùng "become closer". "Become" diễn tả sự thay đổi, và "closer" là tính từ so sánh hơn của "close", nghĩa là "gần gũi hơn". Cụm từ này diễn tả chính xác ý rằng các thành viên trong gia đình trở nên gần gũi nhau hơn em nhé. </explanation>
<explanation id="2"> Trong tiếng Anh, chúng ta không dùng "recharge battery life" để nói về con người. Thay vào đó, chúng ta có thể dùng "recharge themselves", nghĩa là "nạp lại năng lượng cho bản thân". Cách diễn đạt này tự nhiên hơn và vẫn giữ được ý nghĩa ban đầu là nhân viên có thể lấy lại năng lượng trước khi quay lại làm việc em nhé.
<explanation id="3"> Mặc dù "enjoying a holiday" không sai, nhưng trong ngữ cảnh này, "having a longer holiday" nghe tự nhiên hơn và trung lập hơn. "Having" đơn giản chỉ việc có kỳ nghỉ dài hơn, không nhất thiết phải thể hiện sự thích thú. Điều này phù hợp hơn với tone chung của đoạn văn, vì tác giả đang nói về cả ưu điểm và nhược điểm của kỳ nghỉ dài em nhé
<explanation id="4"> Sau cụm "even though" (mặc dù), chúng ta không nên kết thúc câu bằng dấu chấm. Thay vào đó, nên dùng dấu phẩy để nối với phần còn lại của câu. Cấu trúc đúng sẽ là: "Even though..., [main clause]." Việc sử dụng dấu phẩy giúp câu văn liền mạch và logic hơn em nhé.
<explanation id="5"> Từ "based" không cần viết hoa vì nó nằm giữa câu và không phải là tên riêng. Trong tiếng Anh, chúng ta chỉ viết hoa chữ cái đầu tiên của câu, tên riêng, hoặc trong một số trường hợp đặc biệt khác. Việc sửa lỗi này giúp bài viết trở nên chuyên nghiệp và đúng quy tắc hơn em nhé.
<explanation id="6"> Cụm "based on the presented arguments" là một cụm phụ đứng đầu câu, nên sau nó cần có dấu phẩy để ngăn cách với mệnh đề chính. Cấu trúc đúng sẽ là: "[Prepositional phrase], [main clause]." Việc sử dụng dấu phẩy giúp câu văn rõ ràng và dễ đọc hơn em nhé.
</comment>
</output>
</example>"""

TASK_DESCRIPTION = f"""<instruction>
*CORRECTED VERSION:
-Requirement:
+ Do not delete any words from the original essay/paragraph.
+ Put the error in the span tag with the id for that span. In the span, the part that needs to be corrected is placed in the <s> tag and the corrected part is placed in the <mark> tag.
+ Check if the mistake is in grammar or vocab and add class="gramarly" or class="vocabulary" in the span tag.
+ Ignore the incorrect capitalization mistakes.

*EXPLANATIONS: A numbered list of explanations for each correction, including:
- Also give explanations for words that are added, not just those that are corrected.
- Thorough Vietnamese explanation for the correction (make it easy and super detailed for a secondary Vietnamese student with A1-A2 level in English to understand).
- With grammatical mistakes, point out the grammar rules or points relating to each mistake before giving an explanation on how to correct it.
- With vocabulary mistakes, this is mostly because students often translate Vietnamese into English in a “word-by-word” manner, thereby creating unnatural collocations, or they often use words without understanding the appropriate context. Therefore, show them why using such vocabulary is unnatural, then suggest how to correct them. (e.g: a Vietnamese student can translate “đi học” to “go study”, as he thinks “đi” = “go”, and “học” = “study”, while the correct vocabulary should be “attend school)
- Use a friendly, instructive tone.
- Don't give examples.
- Requirement: incorporate "em nhé" (without a comma before “em nhé”) at the end of each explanation to make the explanation sentence more friendly.
- Focus primarily on Lexical Resource (LR) and Grammatical Range and Accuracy (GR) in your corrections and explanations. Do not suggest any replacements for existing linking devices whether they are used correctly or not.
</instruction>"""

TONE_CONTEXT = f"""You are an expert in correcting IELTS essays and explaining mistakes in Vietnamese. Analyze and correct the following IELTS essay.
Based on the essay, proceed with these tasks in <instruction> tag with the above input."""

OUTPUT_FORMATTING = """Your response should follow this structure:
<repair>
(Include the corrected essay here with appropriate corrections as described in the original prompt)
</repair>
<comment>
<explanation id = (id of the span)> (Vietnamese explanation) </explanation>
<explanation id = (id of the span)> (Vietnamese explanation) </explanation>
(Continue the list as needed)
</comment>
"""