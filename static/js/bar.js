var myChart = echarts.init(document.getElementById('bar'));
// 数据准备
var data1 = [ '上衣', '外套', '裤子', '长袖', '短袖', '衬衫', '皮鞋', '运动鞋', '帽子' ];
var data2 = [ '278', '290', '180', '200', '300', '295', '199', '210', '300' ]

var option = {
	// 标题
	title : {
		text : '各产品销量柱状图'
	},
	// 提示框
	tooltip : {},
	// 图例
	legend : {
		data : [ '产品' ]
	},
	// x，y坐标和对应的数据
	xAxis : {
		data : data1
	},
	yAxis : {},
	// 为图标指定系列项，用来指定图标的显示类型、显示名称、显示数据
	series : [ {
		name : '产品',
		type : 'bar',
		data : data2
	} ]
};

myChart.setOption(option);