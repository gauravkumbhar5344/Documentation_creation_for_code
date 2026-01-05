<%@ taglib uri="http://java.sun.com/jsp/jstl/core" prefix="c" %>
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8"/>
    <title>Todo List</title>
</head>
<body>
    <h1>Todo List</h1>
    <ul>
        <c:forEach var="t" items="${todos}">
            <li>${t.title} - <c:out value="${t.completed ? 'Done' : 'Pending'}"/></li>
        </c:forEach>
    </ul>
</body>
</html>
