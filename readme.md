# Python Test

## The task

You have a csv file containing access to your website. Your task is to convert this csv file to an HTML table. Since this is a big dataset you'll have to split it into multiple files.

<table>
<tr>
<th>#</th>
<th>ip_address</th>
<th>country</th>
<th>date</th>
</tr>
<tr>
<td>1</td>
<td>xxx.xxx.xxx.xxx</td>
<td>BELGIUM</td>
<td>12/12/2012</td>
</tr>
<tr>
<td>2</td>
<td>xxx.xxx.xxx.xxx</td>
<td>ITALY</td>
<td>12/12/2012</td>
</tr>
</table>

## Requirements

### Must have :
- Create 10 HTML files `ip_data1.html`, `ip_data2.html`, ..., `ìp_data10.html` containing a `<table>` with the log entries.
- Display the elapsed time once the script has finished the rendering.

### Nice to have :
- Sort the table by date
- Instead of splitting the file by id, split the files by country and create an `unknown.html` file for the null countries

![nice](nice.gif)