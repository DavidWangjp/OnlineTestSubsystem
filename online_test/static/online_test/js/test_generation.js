let data_save;
$(document).ready(function () {
    data_save = data;
    $('#btn-search-problem').click(function () {
        const post_data = {};
        post_data["type"] = 2;
        post_data["creator"] = $("#creator").val();
        post_data["subject"] = $("#subject").val();
        post_data["chapter"] = $("#chapter").val();
        post_data["knowledge_point"] = $("#knowledge-point").val();

        $.ajax({
            url: data_save.problem_search_url,
            type: 'post',
            dataType: 'json',
            data: post_data,
            async: false,
            success: function (data) {
                $("#problem-table-body").empty("");
                let problems = data["infos"];

                let judge_problems = problems['judge'];
                for (let index in judge_problems) {
                    let table = $('#problem-table-body');
                    let new_tr = $("<tr>" +
                        "<td class='hidden'>"  +judge_problems[index][index]["pk"] + "</td>" +
                        "<td>" + "判断" + "</td>" +
                        "<td>" + judge_problems[index][index]["subject"] + "</td>" +
                        "<td>" + judge_problems[index][index]["chapter"] + "</td>" +
                        "<td>" + judge_problems[index][index]["knowledge_point"] + "</td>" +
                        "<td>" + "2018-01-12" + "</td>" +
                        "<td><button class='btn btn-primary btn-static-problem-detail' style='height:80%'>详细 </button></td>" +
                        "<td><button class='btn btn-primary btn-insert-test-problem' style='height:80%'> 添加到当前试卷</button></td>" +
                        "</tr>");
                    new_tr.appendTo(table);
                }

                let choice_problem = problems['choice'];
                for (let index in choice_problem) {
                    let table = $('#problem-table-body');
                    let new_tr = $("<tr>" +
                        "<td class='hidden'>"  +choice_problem[index][index]["pk"] + "</td>" +
                        "<td>" + "选择" + "</td>" +
                        "<td>" + choice_problem[index][index]["subject"] + "</td>" +
                        "<td>" + choice_problem[index][index]["chapter"] + "</td>" +
                        "<td>" + choice_problem[index][index]["knowledge_point"] + "</td>" +
                        "<td>" + "2018-01-12" + "</td>" +
                        "<td><button class='btn btn-primary btn-static-problem-detail' style='height:80%'>详细 </button></td>" +
                        "<td><button class='btn btn-primary btn-insert-test-problem' style='height:80%'> 添加到当前试卷</button></td>" +
                        "</tr>");
                    new_tr.appendTo(table);
                }
                console.log(data);
            },
            error: function (msg) {
                console.log('failure');
                console.log(msg);
            }
        });
    });

    $(document).on('click', '.btn-insert-test-problem', function () {
       let table = $('#test-content-table-body');
       let new_tr = $('<tr></tr>');
       let pk = $(this).parent().parent().children("td:nth-child(1)").text();
       let old_row = $(this).parent().parent();

       let col = $("<td class='hidden'>"+pk+"</td>");
       new_tr.append(col);
       col = $("<td>"+old_row.children("td:nth-child(2)").text()+"</td>");
       new_tr.append(col);
       col = $("<td>"+old_row.children("td:nth-child(3)").text()+"</td>");
       new_tr.append(col);
       col = $("<td>"+old_row.children("td:nth-child(4)").text()+"</td>");
       new_tr.append(col);
       col = $("<td>"+old_row.children("td:nth-child(5)").text()+"</td>");
       new_tr.append(col);
       col = $("<td>"+"2018-05-06"+"</td>");
       new_tr.append(col);
       col = $( "<td><button  class='btn btn-primary btn-static-problem-detail' style='height:80%'>详细</button></td>");
       new_tr.append(col);
       col = $( "<td><button class='btn btn-primary btn-delete-test-problem' style='height:80%'> 从当前试卷删除 </button></td>");
       new_tr.append(col);
       new_tr.appendTo(table);
    });

    $(document).on('click', '#problem-search .btn-static-problem-detail', function () {
        let pk = $(this).parent().parent().children("td:nth-child(1)").text();
        console.log(pk);
        let type = $(this).parent().parent().children("td:nth-child(2)").text();

        if (type == '判断') {
            window.open(data_save.static_judge_detail_url);
        } else {
            window.open(data_save.static_choice_detail_url);
        }
    });

    $(document).on('click', '#test-content .btn-static-problem-detail', function () {
        let pk = $(this).parent().parent().children("td:nth-child(1)").text();
        console.log(pk);
        let type = $(this).parent().parent().children("td:nth-child(3)").text();

        if (type == '判断') {
            window.open(data_save.static_judge_detail_url+'?pk='+pk);
        } else {
            window.open(data_save.static_choice_detail_url+'?pk='+pk);
        }
    });

    $(document).on('click', '.btn-delete-test-problem', function () {
        console.log('hello');
       $(this).parent().parent().remove();
    });

    $('#init-auto-test').click(function () {
        cur_test.name = $("#auto-test-name").val();
        cur_test.subject = $("#auto-test-subject").val();
        cur_test.start_time = $("#auto-test-start-time").val();
        cur_test.end_time = $("#auto-test-end-time").val();
        cur_test.questions = [];
        const post_data = {};
        post_data["name"] = data_save.test.name;
        post_data["subject"] = data_save.test.subject;
        post_data["start_time"] = data_save.test.start_time;
        post_data["end_time"] = data_save.test.end_time;
        post_data["chapter"] = $("#auto-test-chapter").val();
        post_data["knowledge_point"] = $("#auto-test-knowledge-point").val();
        post_data["choice_num"] = $("#auto-test-choice-num").val();
        post_data["judge_num"] = $("#auto-test-judge-num").val();

        $.ajax({
            url: data_save.judge_url,
            type: 'post',
            dataType: 'json',
            data: post_data,
            async: false,
            success: function (data) {
                console.log(data)
                cur_test.questions = data;
            },
            error: function (msg) {
                console.log("failure");
                console.log(msg);
            }
        });
    });
    $('#init-manual-test').click(function () {
        const post_data = {};
        cur_test.name = $("#manual-test-name").val();
        cur_test.subject = $("#manual-test-subject").val();
        cur_test.start_time = $("#manual-test-start-time").val();
        cur_test.end_time = $("#manual-test-end-time").val();
        cur_test.questions = [];

        $("#test-content-table-body").find("tr").each(function(){
            let tdArr = $(this).children();
            let question = {};
            question['pk'] = tdArr.eq(0).text();
            cur_test.questions.push(question);

        });
        post_data['test'] = cur_test;

        $.ajax({
            url: data_save.judge_url,
            type: 'post',
            dataType: 'json',
            data: post_data,
            async: false,
            success: function (data) {
                if (data['result'] === "ok")
                    alert('提交成功');
            }
        });
    });

    $('#submit-test').click(function () {
        const post_data = {};
        post_data["name"] = data_save.test.name;
        post_data["subject"] = data_save.test.subject;
        post_data["start_time"] = data_save.test.start_time;
        post_data["end_time"] = data_save.test.end_time;
        let questions = [];
        $("#test-content-table-body").find("tr").each(function(){
            let tdArr = $(this).children();
            let question = {};
            question['pk'] = tdArr.eq(0).text();
            questions.push(question);

        });
        post_data["questions"] = questions;
        console.log(post_data);

        $.ajax({
            url: data_save.test_add_url,
            type: 'post',
            dataType: 'json',
            data: post_data,
            async: false,
            success: function (data) {
                if (data['result'] === "ok")
                    alert('提交成功');
            }
        });
    });

});