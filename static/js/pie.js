var myChart = echarts.init(document.getElementById('pie'));
var data1 = [ '上衣', '外套', '裤子', '长袖', '短袖', '衬衫', '皮鞋', '运动鞋', '帽子' ];
var data2 = [ '278', '290', '180', '200', '300', '295', '199', '210', '300' ]
var option = {
	title : {
		text : '各产量销售饼状图'
	},
	tooltip : {},
	legend : {
		data : [ '产品' ]
	},
	series : [ {
		name : '产品',
		type : 'pie',
		data : [ {
			name : data1[0],
			value : data2[0]
		}, {
			name : data1[1],
			value : data2[1]
		}, {
			name : data1[2],
			value : data2[2]
		}, {
			name : data1[3],
			value : data2[3]
		}, {
			name : data1[4],
			value : data2[4]
		}, {
			name : data1[5],
			value : data2[5]
		}, {
			name : data1[6],
			value : data2[6]
		}, {
			name : data1[7],
			value : data2[7]
		}, {
			name : data1[8],
			value : data2[8]
		} ]
	} ]
};
myChart.setOption(option);