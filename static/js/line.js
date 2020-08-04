var myChart = echarts.init(document.getElementById('line'));
var data1 = [ '上衣', '外套', '裤子', '长袖', '短袖', '衬衫', '皮鞋', '运动鞋', '帽子' ];
var data2 = [ '278', '290', '180', '200', '300', '295', '199', '210', '300' ]
var option = {
	title : {
		text : '各产品销售折线图'
	},
	tooltip : {},
	legend : {
		data : [ '产品' ]
	},
	xAxis : {
		data : data1
	},
	yAxis : {},
	series : [ {
		name : '产品',
		type : 'line',
		data : data2
	} ]
};

myChart.setOption(option);