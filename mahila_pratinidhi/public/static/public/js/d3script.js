//d3

function call_d3(sample){


  //alert("pasyo");
console.log("checkgaram",d3.select('svg'));

const svg = d3.select('svg');
const svgContainer = d3.select('.graphHolder');
const margin = 50;
const width = 700 - 2 * margin;
const height = 350 - 2 * margin;
const bar_width =30;
var zoom =d3.zoom().scaleExtent([1,1.3]).on("zoom",function(){
    svg2.attr("transform",d3.event.transform)
})

const svg2 = svg
.attr("width","100%")
.attr("height","100%")
//.call(zoom)
.append('g')

const chart = svg2
 //  .attr("width","100%")
 //  .attr("height","100%")
 //  .call(zoom)
 // .append('g')
  .attr('transform', `translate(${margin}, ${margin})`);

const xScale2 = d3.scaleBand()
  .range([0, width])
  .domain(sample.map((s) => s.language))
  .padding(1)

  const xScale = d3.scaleLinear()
    .range([0, width])
    .domain([15, 95]);


const yScale = d3.scaleLinear()
  .range([height, 0])
  .domain([0, 100]);

// vertical grid lines
// const makeXLines = () => d3.axisBottom()
//   .scale(xScale)

const makeYLines = () => d3.axisLeft()
  .scale(yScale)

chart.append('g')
  .attr('transform', `translate(0, ${height})`)
  .call(d3.axisBottom(xScale).tickValues(d3.range(20, 90, 5)));

chart.append('g')
  .call(d3.axisLeft(yScale));

// vertical grid lines
// chart.append('g')
//   .attr('class', 'grid')
//   .attr('transform', `translate(0, ${height})`)
//   .call(makeXLines()
//     .tickSize(-height, 0, 0)
//     .tickFormat('')
//   )

chart.append('g')
  .attr('class', 'grid')
  .call(makeYLines()
    .tickSize(-width, 0, 0)
    .tickFormat('')

  )

const barGroups = chart.selectAll()
  .data(sample)
  .enter()
  .append('g')

barGroups
  .append('rect')
  .attr('class', 'bar')
  .attr('x', (g) => xScale(g.language))
  .attr('y', (g) => yScale(g.value))
  .attr('height', (g) => height - yScale(g.value))
  .attr('width', bar_width ) //xScale.bandwidth()
  .on('mouseenter', function (actual, i) {
    d3.selectAll('.value')
      .attr('opacity', 0)


    d3.select(this)
      .transition()
      .duration(300)
      .attr('opacity', 0.6)
      .attr('x', (a) => xScale(a.language) - 5)
      .attr('width', bar_width + 10) //xScale.bandwidth()

    const y = yScale(actual.value)

    var line = chart.append('line')
      .attr('id', 'limit')
      .attr('x1', 0)
      .attr('y1', y)
      .attr('x2', width)
      .attr('y2', y)

    // barGroups.append('text')
    //   .attr('class', 'divergence')
    //   .attr('x', (a) => xScale(a.language) +  bar_width/ 2) //xScale.bandwidth()
    //   .attr('y', (a) => yScale(a.value) + 30)
    //   .attr('fill', 'white')
    //   .attr('text-anchor', 'middle')
    //   .text((a, idx) => {
    //     const divergence = (a.value - actual.value).toFixed(1)
    //
    //     let text = ''
    //     if (divergence > 0) text += '+'
    //     text += `${divergence}%`
    //
    //     return idx !== i ? text : '';
    //   })

  })
  .on('mouseleave', function () {
    d3.selectAll('.value')
      .attr('opacity', 1)

    d3.select(this)
      .transition()
      .duration(300)
      .attr('opacity', 1)
      .attr('x', (a) => xScale(a.language))
      .attr('width', bar_width) //xScale.bandwidth()

    chart.selectAll('#limit').remove()
    chart.selectAll('.divergence').remove()
  })

barGroups
  .append('text')
  .attr('class', 'value')
  .attr('x', (a) => xScale(a.language) + bar_width / 2) //xScale.bandwidth()
  .attr('y', (a) => yScale(a.value) + 30)
  .attr('text-anchor', 'middle')
  .text((a) => `${a.value}%`)

svg
  .append('text')
  .attr('class', 'label')
  .attr('x', -(height / 2) - margin)
  .attr('y', margin / 2.4)
  .attr('transform', 'rotate(-90)')
  .attr('text-anchor', 'middle')
  .text('frequency(%)')

svg.append('text')
  .attr('class', 'label')
  .attr('x', width / 2 + margin)
  .attr('y', height+margin*1.7)
  .attr('text-anchor', 'middle')
  .text('Age')

svg.append('text')
  .attr('class', 'title')
  .attr('x', width / 2 + margin)
  .attr('y', 0.7*margin)
  .attr('text-anchor', 'middle')
  .text('Age Variation across in 2018')

svg.append('text')
  .attr('class', 'source')
  .attr('x', width - margin)
  .attr('y', height-margin)
  .attr('text-anchor', 'start')
  .text('Source: Election, 2018')



} //end of call_d3 fucntion
