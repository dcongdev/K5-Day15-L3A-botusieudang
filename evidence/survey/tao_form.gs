/**
 * Tạo Google Form khảo sát "tra luật nộp bài hackathon" — nhóm botusieudang.
 * Cách dùng: mở https://script.google.com → New project → xoá hết code mẫu → dán file này → bấm Run (hàm taoForm)
 * → cho phép quyền (Review permissions → chọn tài khoản → Advanced → Go to … → Allow)
 * → xem link ở View → Logs (hoặc Execution log).
 * Đáp án câu 2, 4, 5, 6 giữ ĐÚNG CHỮ dưới đây: evidence/survey/count_survey.py so khớp theo chữ.
 */
function taoForm() {
  var form = FormApp.create('Khảo sát: tra luật nộp bài hackathon AI20K (2 phút)');
  form.setDescription(
    'Nhóm mình đang tìm hiểu cách các bạn tra luật nộp bài hackathon (file nào commit, hạn từng mốc, format…). ' +
    '2 phút, 9 câu, không giới thiệu sản phẩm, không thu tên. Thành viên nhóm botusieudang vui lòng không điền.');
  form.setCollectEmail(false);
  form.setLimitOneResponsePerUser(false);

  form.addMultipleChoiceItem()
    .setTitle('1. Trong nhóm hackathon, bạn là:')
    .setChoiceValues(['Đội trưởng', 'Người giữ repo', 'Thành viên khác'])
    .setRequired(true);

  form.addMultipleChoiceItem()
    .setTitle('2. Lần gần nhất bạn phải tra hoặc hỏi lại một luật nộp bài (file nào commit, hạn mốc, format TEAMS.md, được sửa gì sau CP2…) là khi nào?')
    .setChoiceValues(['Hôm nay', 'Hôm qua', '2–7 ngày trước', 'Lâu hơn', 'Chưa bao giờ'])
    .setRequired(true);

  form.addParagraphTextItem()
    .setTitle('3. Lần đó bạn cần biết điều gì? (ghi gần đúng câu bạn đã hỏi / đã tìm)');

  form.addCheckboxItem()
    .setTitle('4. Lần đó bạn đã làm thế nào? (chọn nhiều)')
    .setChoiceValues(['lục README / guide / rubric', 'hỏi nhóm chat lớp', 'hỏi lab coach / TA',
                      'hỏi bạn cùng nhóm', 'hỏi ChatGPT / AI khác', 'đoán rồi làm'])
    .showOtherOption(true);

  form.addMultipleChoiceItem()
    .setTitle('5. Lần đó mất bao lâu đến khi có câu trả lời bạn tin được?')
    .setChoiceValues(["Dưới 2'", "2–5'", "5–15'", "15–30'", "Trên 30'", 'Không tìm ra']);

  form.addMultipleChoiceItem()
    .setTitle('6. Lần đó bạn đã mở bao nhiêu file / hỏi bao nhiêu người?')
    .setChoiceValues(['1', '2', '3', '4+']);

  form.addTextItem()
    .setTitle('7. Trong 1 tuần qua, bạn tra / hỏi luật nộp bài khoảng mấy lần? (ghi số)')
    .setValidation(FormApp.createTextValidation().requireNumber().build());

  form.addParagraphTextItem()
    .setTitle('8. Đã có lần nào nhóm bạn nộp sai / sửa nhầm vì hiểu sai luật chưa?')
    .setHelpText('Ghi "Không", hoặc "Có — " rồi kể ngắn.');

  form.addTextItem()
    .setTitle('9. (tuỳ chọn) Cho nhóm hỏi thêm 10 phút được không? Để lại cách liên hệ nếu đồng ý.');

  var ss = SpreadsheetApp.create('Kết quả khảo sát tra luật nộp bài (raw — KHÔNG commit)');
  form.setDestination(FormApp.DestinationType.SPREADSHEET, ss.getId());

  Logger.log('Link GỬI cho mọi người: ' + form.getPublishedUrl());
  Logger.log('Link SỬA form: ' + form.getEditUrl());
  Logger.log('Sheet kết quả: ' + ss.getUrl());
}
