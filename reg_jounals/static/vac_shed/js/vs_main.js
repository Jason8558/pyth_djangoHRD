function end_count(date_from, days) {
  date_from_new = date_from.split('-')[2] + '.' + date_from.split('-')[1] + '.' + date_from.split('-')[0]

if (days) {
  date_to = Date.parse(date_from_new).addDays(parseInt(days, 10)-1)}
else {
    date_to = Date.parse(date_from_new).addDays(parseInt(days2, 10))
}

console.log(date_to.toString('yyyy-MM-dd'));

  return(date_to.toString('yyyy-MM-dd'))
}

function celebrates(date_from, date_to, id) {
  date_from = date_from.split('-')[2] + '.' + date_from.split('-')[1] + '.' + date_from.split('-')[0]
  date_to = date_to.split('-')[2] + '.' + date_to.split('-')[1] + '.' + date_to.split('-')[0]


  jan = [1,2,3,4,5,6,7,8]
  feb = [23]
  mar = [8]
  may = [1,9]
  jun = [12]
  nov = [4]

  total_celebrate = 0

  day_from = date_from.split('.')[0]
  month_from = date_from.split('.')[1]
  year_from = date_from.split('.')[2]

  day_to = date_to.split('.')[0]
  month_to = date_to.split('.')[1]
  year_to = date_to.split('.')[2]

if (day_from[0] == 0) {
  day_from = day_from[1]
}


if (day_to[0] == 0) {
  day_to = day_to[1]
}



  if (month_from != month_to) {
    switch (month_from) {
      case '01':
          for (var day of jan) {
            if (day_from <= day) {
              total_celebrate = total_celebrate + 1
              console.log(total_celebrate);
            }
          }
        break;

      case '02':
          for (var day of feb) {
            if (day_from <= day) {
              total_celebrate = total_celebrate + 1
              console.log(total_celebrate);
            }
          }
        break;

        case '03':
            for (var day of mar) {
              if (day_from <= day) {
                total_celebrate = total_celebrate + 1
                console.log(total_celebrate);
              }
            }
          break;

          case '05':
          for (var day of may) {
            if (day_from <= day) {
              total_celebrate = total_celebrate + 1
              console.log(total_celebrate);
            }
          }
          break;

          case '06':
          for (var day of jun) {
            if (day_from <= day) {
              total_celebrate = total_celebrate + 1
              console.log(total_celebrate);
            }
          }
          break;

          case '11':
          for (var day of nov) {
            if (day_from <= day) {
              total_celebrate = total_celebrate + 1
              console.log(total_celebrate);
            }
          }
          break;

          default:

        }


  switch (month_to) {
    case '01':
        for (var day of jan) {
          if (day_to >= day) {
            total_celebrate = total_celebrate + 1
            console.log(total_celebrate);
          }
        }
      break;

      case '02':
          for (var day of feb) {
            if (day_to >= day) {
              console.log(day_to);
              total_celebrate = total_celebrate + 1
              console.log(total_celebrate);
            }
          }
        break;

        case '03':
            for (var day of mar) {
              if (day_to >= day) {
                total_celebrate = total_celebrate + 1
                console.log(total_celebrate);
              }
            }
          break;

          case '05':
          for (var day of may) {
            if (day_to >= day) {
              total_celebrate = total_celebrate + 1
              console.log(total_celebrate);
            }
          }
          break;

          case '06':
          for (var day of jun) {
            if (day_to >= day) {
              total_celebrate = total_celebrate + 1
              console.log(total_celebrate);
            }
          }
          break;

          case '11':
          for (var day of nov) {
            if (day_to >= day) {
              total_celebrate = total_celebrate + 1
              console.log(total_celebrate);
            }
          }
          break;

          default:


  }

  }

date_to = Date.parse(date_to).addDays(parseInt(total_celebrate, 10));





console.log($('per' + id + ' #per-date-to').val());

$('#per' + id + ' #per-date-to').val(date_to.toString('yyyy-MM-dd'))



}
