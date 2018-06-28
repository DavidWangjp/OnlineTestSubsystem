let data_save;
$(document).ready(function () {
    data_save = data;
    $('#btn-search-problem').click(function () {
        const post_data = {};
        post_data["type"] = 0;
        post_data["creator"] = $("#creator").val();
        post_data["subject"] = $("#subject").val();
        post_data["chapter"] = $("#chapter").val();
        post_data["knowledge_point"] = $("#knowledge-point").val();


        $.ajax({
            url: data_save.problem_search_url,
            method: 'post',
            dataType: 'json',
            data: post_data,
            async: false,
            success: function (data) {
                console.log(data);
                $("#choice-problem-table-body").empty("");
                for (var i = 0; i < 5; i++) {
                    let table = $('#choice-problem-table-body');

                    let new_tr = $("<tr>" +
                        "<td class='hidden'>"  + "he" + "</td>" +
                        "<td>" + "数学faflajfla f".slice(0, 10) +"..."+ "</td>" +
                        "<td>" + "数学" + "</td>" +
                        "<td>" + "ch4" + "</td>" +
                        "<td>" + "函数" + "</td>" +
                        "<td>" + "2018-01-12" + "</td>" +
                        "<td><button class='btn btn-primary btn-problem-detail' style='height:80%'>详细 </button></td>" +
                        "</tr>");
                    new_tr.appendTo(table);
                }

                $("#judge-problem-table-body").empty("");
                for (var i = 0; i < 3; i++) {
                    let table = $('#judge-problem-table-body');

                    let new_tr = $("<tr>" +
                        "<td class='hidden'>"  + "he" + "</td>" +
                        "<td>" + "数学faflajfla f".slice(0, 10) +"..."+ "</td>" +
                        "<td>" + "数学" + "</td>" +
                        "<td>" + "ch2" + "</td>" +
                        "<td>" + "函数" + "</td>" +
                        "<td>" + "2018-01-12" + "</td>" +
                        "<td><button class='btn btn-primary btn-problem-detail' style='height:80%'>详细 </button></td>" +
                        "</tr>");
                    new_tr.appendTo(table);
                }
            },
            error: function (msg) {
                console.log('error');
                console.log(msg);
            }
        });
    });
    $('#btn-single-problem-nav').click(function () {
       window.open(data_save.problem_detail_url);
    });
    $(document).on('click', '.btn-problem-detail', function () {
        let pk = $(this).parent().parent().children("td:nth-child(1)").text();
        console.log(pk);
        if ($('#choice_problem').is('.active')) {
             window.open(data_save.problem_choice_detail_url+'?pk='+pk);
        } else {
            window.open(data_save.problem_judge_detail_url+'?pk='+pk);
        }
    });

    $('#btn-insert-problem').click(function () {
        const post_data = {};

        let type = $('#choice_problem').is('.active')?1:0;
        console.log(type);
        post_data["type"] = type;
        post_data["content"] = $('#content').val();
        if (type == 1) {
            post_data["choice_a"] = $("#choice_a").val();
            post_data["choice_b"] = $("#choice_b").val();
            post_data["choice_c"] = $("#choice_c").val();
            post_data["choice_d"] = $("#choice_d").val();
        }
        post_data["solution"] = $("#solution").val();
        post_data["score"] = $("#score").val();
        post_data["subject"] = $("#subject").val();
        post_data["chapter"] = $("#chapter").val();
        post_data["knowledge_point"] = $("#knowledge_point").val();


        $.ajax({
            url: data_save.problem_add_url,
            type: 'post',
            dataType: 'json',
            data: post_data,
            async: false,
            success: function (data) {
                if (data['result'] === "ok")
                    alert('添加成功');
            },
            error: function (msg) {
                console.log('error');
                console.log(msg);
            }
        });
    });
    $('#btn-update-problem').click(function () {
        const post_data = {};

        let type = $('#choice_problem').is('.active')?1:0;
        post_data["type"] = type;
        post_data["content"] = $('#content').val();
        if (type == 1) {
            post_data["choice_a"] = $("#choice_a").val();
            post_data["choice_b"] = $("#choice_b").val();
            post_data["choice_c"] = $("#choice_c").val();
            post_data["choice_d"] = $("#choice_d").val();
        }
        post_data["solution"] = $("#solution").val();
        post_data["score"] = $("#score").val();
        post_data["subject"] = $("#subject").val();
        post_data["chapter"] = $("#chapter").val();
        post_data["knowledge_point"] = $("#knowledge_point").val();


        $.ajax({
            url: data_save.problem_mod_url,
            type: 'post',
            dataType: 'json',
            data: post_data,
            async: false,
            success: function (data) {
                if (data['result'] === "ok")
                    alert('更新成功');
            },
            error: function (msg) {
                console.log('error');
                console.log(msg);
            }

        });
    });
    $('#btn-delete-problem').click(function () {
        const post_data = {};

        let type = $('#choice_problem').is('.active')?1:0;
        post_data["type"] = type;
        post_data["content"] = $('#content').val();
        if (type == 1) {
            post_data["choice_a"] = $("#choice_a").val();
            post_data["choice_b"] = $("#choice_b").val();
            post_data["choice_c"] = $("#choice_c").val();
            post_data["choice_d"] = $("#choice_d").val();
        }
        post_data["solution"] = $("#solution").val();
        post_data["score"] = $("#score").val();
        post_data["subject"] = $("#subject").val();
        post_data["chapter"] = $("#chapter").val();
        post_data["knowledge_point"] = $("#knowledge_point").val();


        $.ajax({
            url: data_save.problem_delete_url,
            type: 'post',
            dataType: 'json',
            data: post_data,
            async: false,
            success: function (data) {
                if (data['result'] === "ok")
                    alert('删除成功');
            },
            error: function (msg) {
                console.log('error');
                console.log(msg);
            }
        });
    });
});
