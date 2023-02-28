const comments = [{title: "title", body: "body"}];
exports.handler = async (event) => {
    if(event.httpMethod === "GET"){
        var response = {
            "body": JSON.stringify(comments)
        };
    }
    else if(event.httpMethod === "POST"){
        let req = JSON.parse(event.body);
        if(req.title && req.body){
            comments.push({title: req.title, body: req.body});
            var response = {
                "body": JSON.stringify(comments)
            };
        }
        else{
            var response = {
                "body": "Invalid request body"
            };
        }
    }
    else{
        var response = {
            "body": "Invalid HTTP method"
        };
    }
    return response;
};
