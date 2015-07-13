<!?DOCTYPE html>
<html>
<head>
<style>
table {
	width: 100%;
	border-collapse: collapse;
}

table, td, th {
	border: 2px solid black;
	padding: 5px;
}

th {text-align: left;}
</style>
</head>
<body>

<?php
$q = intval($_GET['q']);

echo $q;

$con = mysqli_connect('localhost', 'root', '******', 'name')
if (!$con){
	die('Connection failed: ' . mysqli_error($con));
}

mysqli_select_db($con,"ajax_demo");
$sql="SELECT * FROM TestStation WHERE id = '".$q."'";
$result = mysqli_query($con,$sql);

echo "<table>
<tr>
<th>test_run</th>
<th>result</th>
<th>start_time</th>
<th>end_time</th>
<th>notes</th>
</tr>";
while($row = mysqli_fetch_array($result))
{
	echo "<tr>";
	echo "<td>" . $row['test_run'] . "</td>";
	echo "<td>" . $row['result'] . "</td>";
	echo "<td>" . $row['start_time'] . "</td>";
	echo "<td>" . $row['end_time'] . "</td>";
	echo "<td>" . $row['notes'] . "</td>";
	echo "<tr>";
}
echo "</table>";
mysqli_close($con);
?>
</body>
</html>